import pandas as pd
df = pd.DataFrame({'rainy':[.4,.7],
                   'sunny':[.6,.3]}
                  ,index=['rainy','sunny'])
print df

print df.dot(df)

themarket = pd.DataFrame({'bull market':[0.9, 0.075, 0.025],
                          'bear market':[0.15, 0.8, 0.05],
                          'stagnant market':[.25, .25, .5]}
                          ,index=['bull market','bear market'
                                  ,'stagnant market'])

print themarket

def marketState(currently, steps):
    x = currently
    for i in range(0,steps):
        x = x.dot(x)
    return x
