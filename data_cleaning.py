import pandas as pd

df = pd.read_csv('data/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
df.dropna(inplace=True)
df.to_csv('data/sales_clean.csv', index=False)
