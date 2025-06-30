import pandas as pd

df = pd.read_csv('data/sales_clean.csv')
summary = df.groupby('Region')['Sales'].sum().reset_index()
summary.to_csv('output/summary.csv', index=False)
