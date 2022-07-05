import pandas as pd
csv_path = 'C:/Users/shubh/Downloads/melb_data.csv'
df = pd.read_csv(csv_path)
#print(df.head())
#print(pd.unique(df))
##print(pd.set_option(df))
print(df)
y = df.Price

#print(y)
df_path = 'C:/Users/shubh/Downloads/'
e = df.to_sql(df_path)