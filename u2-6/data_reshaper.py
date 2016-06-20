import pandas as pd
import numpy as np

df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)
'https://github.com/Teej13/TJCode/blob/master/LoanStats3b.csv'
'https://github.com/CorySimon/lendingClub/blob/master/data/LoanStats3b.csv.zip'

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']
