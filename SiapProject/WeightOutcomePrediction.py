from __future__ import print_function, division

#%matplotlib inline

import numpy as np
import pandas as pd

import random
import thinkplot
import readData
import statFunctions

df = readData.ReadFemPreg()

training_set = readData.GetTrainingData(df)
print(len(training_set))

test_set = readData.GetTestData(df)
print(len(test_set))

import first

live, firsts, others = first.MakeFrames()

import statsmodels.formula.api as smf

formula = 'totalwgt_kg ~ agepreg'
model = smf.ols(formula, data=live)
results = model.fit()
print(results.summary())