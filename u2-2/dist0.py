import collections

# part 1 =================
testlist = [1,4,5,6,9,9,9]

c = collections.Counter(testlist)

print(c)

count_sum = sum(c.values())

for k,v in c.iteritems():
    print("The frequency of number " + str(k) + " is " +
          str(float(v) / count_sum))

# part 2 =================    
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5
     , 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.boxplot(x)
plt.show()
'''
You can save the plot by using the savefig() function in pyplot
instead of show(). You call it on the plt object and pass in the
filename you wish to use. For example, to save the file
as "boxplot.png", you'd type plt.savefig("boxplot.png").
This will save the current plt object with the filename you specified.
'''

plt.hist(x, histtype='bar')
plt.show()

# part 3 =================

import numpy as np
import scipy.stats as stats

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() # this will generate the first graph

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()


