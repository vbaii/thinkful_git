''' linear regression assumes a continuous response from a continuous input.
Logistic regression aaplies to the class of variables that exists as
discrete values, like 'yes' or 'no' overweight/underwiehgt, etc. '''

# odds ratios: probability of one thing happening compared to another

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('../loansData.csv')

# clean interest rate, fico, loan length
loansData['Interest.Rate'] = [float(int_rate[:-1])/100 for int_rate in loansData['Interest.Rate']]
loansData['FICO.Score'] = [int(score_range.split('-')[0]) for score_range in loansData['FICO.Range']]
loansData['Loan.Length'] = [int(term[:-7]) for term in loansData['Loan.Length']]


loansData['IR_TF'] = loansData['Interest.Rate'] < 0.12
loansData['constant_intercept'] = 1.0

ind_vars =['FICO.Score','Amount.Funded.By.Investors','constant_intercept']
