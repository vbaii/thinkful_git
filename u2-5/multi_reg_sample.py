# makes a 3D plot of a 2-variable model to predict Sales
# based on TV and Radio
# http://nbviewer.jupyter.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb#appendix
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
'''
df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv'
                     , index_col=0)
'''
df_adv = pd.read_csv('Advertising.csv', index_col=0)

X = df_adv[['TV','Radio']]
y = df_adv['Sales']

## fit an Ordinary-Least-Squares (OLS) model with intercept on TV and Radio
X = sm.add_constant(X)
est = sm.OLS(y,X).fit()

## Create the 3d plot -- skip reading this
# TV/Radio grid for 3d plot
xx1, xx2 = np.meshgrid(np.linspace(X.TV.min(), X.TV.max(), 100),
            np.linspace(X.Radio.min(), X.Radio.max(), 100))
# plot the hyperplane by eveluation the parameters on the grid
Z = est.params[0] + est.params[1] * xx1 + est.params[2] * xx2

# create matplotlib 3d axes
fig = plt.figure(figsize=(12,8))
ax = Axes3D(fig, azim=-115, elev=15)

# plot hyperplane
surf = ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.6, linewidth=0)

# plot data points - points over the HP are white, points below are black
resid = y - est.predict(X)
ax.scatter(X[resid >= 0].TV, X[resid >=0].Radio, y[resid >= 0], color='black'
           ,alpha=1.0, facecolor='white')
ax.scatter(X[resid < 0].TV, X[resid < 0].Radio, y[resid < 0], color='black'
           ,alpha=1.0)

# set axis labels

ax.set_xlabel('TV')
ax.set_ylabel('Radio')
ax.set_zlabel('Sales')

plt.show()
