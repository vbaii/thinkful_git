import pandas as pd
from scipy import stats
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


oldphrase = 'The {} for the Alcohol and Tobacco dataset is {}' 
phrase = 'The {} for the {} dataset is {}' 

def printSet(something):
    theSet = {}
    theSet['mean'] = something.mean()
    theSet['median'] = something.median()
    theSet['mode'] = stats.mode(something)
    theSet['standard deviation'] = something.std()
    theSet['variance'] = something.var()
    theSet['range'] = max(something) - min(something)
    return theSet

# df.Alcohol.mean()
# df.Tobacco.mean()
# stats.mode(df.Alcohol)
# stats.mode(df.Tobacco)
# 'range' max(df['Alcohol']) - min(df['Alcohol']) # 2.4500000000000002
# 'standard dev' df['Alcohol'].std() # 0.79776278087252406
# 'variance' df['Alcohol'].var() # 0.63642545454546284


alc_set = printSet(df.Alcohol)
tob_set = printSet(df.Tobacco)

for item in alc_set:
    if item == 'mode':
        print phrase.format(item, 'Alcohol', alc_set[item].mode[0])
    else:
        print phrase.format(item, 'Alcohol',  alc_set[item])

for item in tob_set:
    if item == 'mode':
        print phrase.format(item, 'Tobacco', tob_set[item].mode[0])
    else:
        print phrase.format(item, 'Tobacco', tob_set[item])


