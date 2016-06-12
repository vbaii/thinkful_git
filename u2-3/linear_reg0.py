import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('loansData.csv')

# loansData['Interest.Rate'].head()
# loansData['Loan.Length'].head()
# loansData['FICO.Range'].head()


# clean interest rate
def interestFix(a_series):
    for indx in range(0,len(a_series)):
        curr = a_series.iloc[indx]
        nxt = curr[:len(curr)-1]
        a_series.iloc[indx] = nxt

interestFix(loansData['Interest.Rate'])
print loansData['Interest.Rate']

# for i in b: a.append(i[:len(i)-1])

# clean fico

#plt fico
'''
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()
'''

# create scatter plt

'top-left_to_bottom-right diagonal is varibale against itself'
# a = pd.scatter_matric(loansData, alpha=0.05, figsize=(0,10))
'makes diagonal a historgram of var instead'
# a = pd.scatter_matric(loansData, alpha=0.05, figsize=(0,10), diagonal='hist')
