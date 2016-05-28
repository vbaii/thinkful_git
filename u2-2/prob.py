import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import collections

millenial = np.random.randint(low=1980, high=2001, size=200)
c = collections.Counter(millenial)
cSum = sum(c.values())

for k,v in c.iteritems():
    print("The frequency of value " + str(k) + " is " +
          str(float(v) / cSum))

plt.boxplot(millenial)
plt.savefig("boxplot.png")

plt.figure()
plt.hist(millenial, histtype='bar')
plt.savefig("histogram.png")

wiser = (millenial - np.mean(millenial))/ np.std(millenial)


plt.figure()
graph = stats.probplot(wiser, dist="norm", plot=plt)
plt.savefig("qq_normalized.png")
