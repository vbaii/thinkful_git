'''
A chi-squared distribution with k degrees of freedom is a distribution
of the sum of the squares of all the k variables, where k is
an independent standard normal random variable. That is, k is
a random variable with a normal distribution and it is not dependent
on any other variable. The chi-squared distribution samples all
of these k's, squares the samples, and then sums them up.
The resultant collection of data is a chi-squared distribution.
'''
 
'''
A chi-square test is simply a hypothesis test that is run on a dataset
to tell you how well your data is modeled by the chi-square distribution
it answers the question, "How well does this data fit my model?"
-hence, goodness of fit.
'''

'''
For example, if we take a poll of students' favorite sports, we
can test if preference is evenly distributed among the possibilities.
Let's say we poll 50 students and there are only 4 sports to chose from.
If preferences were evenly distributed, we would expect 12.5 students
to choose each sport. To test this hypothesis, we would calculate

(observed * count-expected * count)^2/(expected * count)

for each sport. The sum of these calculations have
a chi-squared distribution with three degrees of freedom.
'''

import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
import collections

loansData = pd.read_csv('loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# plt.figure()
# plt.bar(freq.keys(), freq.values(), width=1)
# plt.show()

chi, p = stats.chisquare(freq.values())

print '''Results:\nchi is: {},\nand p is: {}'''.format(chi,p)
