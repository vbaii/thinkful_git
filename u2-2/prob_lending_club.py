import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('loansData.csv')
# loansData.info()
loansData.dropna(inplace=True)

amountFunded = loansData['Amount.Funded.By.Investors']
amountRequested = loansData['Amount.Requested']

plt.boxplot(amountRequested.values)
plt.savefig("boxplot_requested.png")

plt.figure()
plt.hist(amountRequested.values, color='#0099ff')
plt.savefig("histogram_requested.png")

plt.figure()
qq_req = stats.probplot(amountRequested.values, dist='norm', plot=plt)
plt.savefig("qq_requested.png")
# plt.show()

# not much difference between funded and requested amounts
