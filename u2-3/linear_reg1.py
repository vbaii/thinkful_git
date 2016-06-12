import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('loansData.csv')

# print loansData['Interest.Rate'].head()
# print loansData['Loan.Length'].head()
# print loansData['FICO.Range'].head()


# clean interest rate
loansData['Interest.Rate'] = [float(int_rate[:-1])/100
                              for int_rate in loansData['Interest.Rate']]
# clean fico
loansData['FICO.Score'] = [int(score_range.split('-')[0])
                           for score_range in loansData['FICO.Range']]
# clean loan length
loansData['Loan.Length'] = [int(term[:-7])
                            for term in loansData['Loan.Length']]

# plt fico
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()


# create scatter plt
'top-left_to_bottom-right diagonal is variable against itself'
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
'makes diagonal a historgram of var instead'
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
