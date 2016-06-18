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

#   --------    --------
# u2-4 part 3

' model of how interest rate vares with FICO and Loan Amount '
# interest_rate = b + a1(FicoScore) + a2(LoanAmount)
' plugging in values '
# interest_rate = b + a1(750) + a2(10000)


' 1. define the logistic regresison model '
# logit = sm.Logit(df[IR_TF'], df[ind_vars])
' 2. fit the model '
# result = logit.fit()
' 3. get the fitted coefficientsfro the results '
# coeff = result.params
# print coeff
' 4. using these coefficients, what is the linear part of our predictor? '
# interest_rate = -60.125 + 0.087243(FicoScore) - 0.000174(LoanAmount)
' 5. what is our logistic function? '
# p(x) = 1/(1 +e^(intercept + 0.087423(FicoScore) - 0.000174(LoanAmount))

def logistic_function(fico, amount):
    intercept, fcoeff, acoeff = 0
    
    pofx_denom = 1 + np.e**(intercept + fcoeff(fico) - acoeff(amount))
    return 1/pofx_denom
