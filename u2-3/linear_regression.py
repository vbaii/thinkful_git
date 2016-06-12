import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('loansData.csv')

'InterestRate = b + a1(FICOScore) + a2(LoanAmount)'

# clean interest rate
loansData['Interest.Rate'] = [float(int_rate[:-1])/100
                              for int_rate in loansData['Interest.Rate']]
# clean fico
loansData['FICO.Score'] = [int(score_range.split('-')[0])
                           for score_range in loansData['FICO.Range']]
# clean loan length
loansData['Loan.Length'] = [int(term[:-7])
                            for term in loansData['Loan.Length']]

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# dependent variable
y = np.matrix(intrate).transpose()
# indedpendent variables, shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# create an input matrix
x = np.column_stack([x1,x2])

# create a linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()
