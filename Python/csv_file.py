import pandas as pd

df = pd.read_csv('<csv file(.csv)>')
print(df.head(5))
print('-------------------------------------------')
print(df.tail(5))

df.info()