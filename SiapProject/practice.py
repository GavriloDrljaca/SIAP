import statFunctions
import thinkplot
import readData
import numpy as np

# Load just live birth pregnancies
preg = readData.ReadFemPreg()
live = preg[preg.outcome == 1]
# Weight distribution for live births
# hist = statFunctions.Hist(round(live.totalwgt_kg, 1), label='birthwgt_kg')
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='Birth weight (kg)', ylabel='Count', title='Weight distribution')
#
# # Age distribution for all births
# ages = np.floor(preg.agepreg)
# hist = statFunctions.Hist(ages, label="respondent_age")
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='Respondent age (years)', ylabel='Count', title='Age distribution')
#
# # Pregnancies length distribution
#
# hist = statFunctions.Hist(live.prglngth, label='pregnancy_length')
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='Pregnancy lenght (weeks)', ylabel='Count', title="Pregnancies length distribution")
#
#
# firsts = live[live.birthord == 1]
# others = live[live.birthord != 1]
# first_hist = statFunctions.Hist(firsts.prglngth, label='firstborn')
# other_hist = statFunctions.Hist(others.prglngth, label='others')
#
# width = 0.4
# thinkplot.PrePlot(2)
# thinkplot.Hist(first_hist, align='right', width=width)
# thinkplot.Hist(other_hist, align='left', width=width)
# thinkplot.Show(xlabel='Pregnancy lenght (weeks)', ylabel='frequency', xlim=[27, 46])

live.prglngth.mean()
var = live.prglngth.var()
std = live.prglngth.std()
