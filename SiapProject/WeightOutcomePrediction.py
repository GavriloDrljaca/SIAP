from __future__ import print_function, division

#%matplotlib inline

import numpy as np
import pandas as pd

import random
import thinkplot
import readData
import statFunctions
import first

live, firsts, others = first.MakeFrames()

import statsmodels.formula.api as smf

def totalwgt_single_prediction():
    formula = 'totalwgt_kg ~ agepreg'
    model = smf.ols(formula, data=live)
    results = model.fit()
    print(results.summary())


def totalwgt_multi(data, alpha):

    formula = ('totalwgt_kg ~ agepreg + C(race) + babysex==1 + '
               'nbrnaliv>1 + paydu==1 + totincr')
    results = smf.ols(formula, data=data).fit()
    print(results.summary())


def totalwgt_multi_lasso(data, alpha):
    """
    Model build using ridge regression (L1_wt = 1.0)
    :param data:
    :param alpha:
    :return:
    """
    formula = ('totalwgt_kg ~ agepreg + C(race) + babysex==1 + '
               'nbrnaliv>1 + paydu==1 + totincr')
    results = smf.ols(formula, data=data).fit_regularized(method='coord_descent',
                                    maxiter=1000, alpha=alpha, L1_wt=1.0, start_params=None, cnvrg_tol=1e-08, zero_tol=1e-08)
    print(results.summary())


def totalwgt_multi_ridge(data, alpha):
    """
    Model build using ridge regression (L1_wt = 0)
    :param data:
    :param alpha:
    :return:
    """
    formula = ('totalwgt_kg ~ agepreg + C(race) + babysex==1 + '
               'nbrnaliv>1 + paydu==1 + totincr')
    results = smf.ols(formula, data=data).fit_regularized(method='coord_descent',
                                    maxiter=1000, alpha=alpha, L1_wt=0.0, start_params=None, cnvrg_tol=1e-08, zero_tol=1e-08)
    print(results.summary())


def prgoutcome_prediction(data):

    model = smf.logit('live_outcome ~ agepreg', data)
    results = model.fit()
    print(results.summary())


df = readData.ReadFemPreg()
df['live_outcome'] = (df.outcome == 1).astype(int)
training_set = readData.GetTrainingData(df)
test_set = readData.GetTestData(df)



#live = live[live.prglngth>30]
resp = readData.ReadFemResp()
resp.index = resp.caseid
join = df.join(resp, on='caseid', rsuffix='_r')

alpha=1e-10
#rss = 0.67
#totalwgt_multi_lasso(join, alpha)

totalwgt_multi_ridge(join, alpha)

#rss = 0.67
#totalwgt_multi(join, 0)
#prgoutcome_prediction(test_set)