"""
This file holds all statistical and other functions
used in this project
"""

from __future__ import print_function, division


"""This file contains class definitions for:

Hist: represents a histogram (map from values to integer frequencies).

Pmf: represents a probability mass function (map from values to probs).

_DictWrapper: private parent class for Hist and Pmf.

Cdf: represents a discrete cumulative distribution function

Pdf: represents a continuous probability density function

"""
import bisect
import copy
import logging
import math
import random
import re

from collections import Counter
from operator import itemgetter

import thinkplot

import numpy as np
import pandas

import scipy
from scipy import stats
from scipy import special
from scipy import ndimage

from io import open


def ReadStataDct(dct_file, **options):
    """Reads a Stata dictionary file.

    dct_file: string filename
    options: dict of options passed to open()

    returns: FixedWidthVariables object
    """
    type_map = dict(byte=int, int=int, long=int, float=float, double=float)

    var_info = []
    for line in open(dct_file, **options):
        match = re.search(r'_column\(([^)]*)\)', line)
        if match:
            start = int(match.group(1))
            t = line.split()
            vtype, name, fstring = t[1:4]
            name = name.lower()
            if vtype.startswith('str'):
                vtype = str
            else:
                vtype = type_map[vtype]
            long_desc = ' '.join(t[4:]).strip('"')
            var_info.append((start, vtype, name, fstring, long_desc))

    columns = ['start', 'type', 'name', 'fstring', 'desc']
    variables = pandas.DataFrame(var_info, columns=columns)

    # fill in the end column by shifting the start column
    variables['end'] = variables.start.shift(-1)
    variables.loc[len(variables) - 1, 'end'] = 0

    dct = FixedWidthVariables(variables, index_base=1)
    return dct
