import pandas as pd
import os

source = os.path.abspath('.')
db_file = os.path.join(source, 'cancelamentos.csv')

table = pd.read_csv(db_file)

table = table.drop(columns='CustomerID')

table = table.dropna()

print(table['cancelou'].value_counts())
print(table['cancelou'].value_counts(normalize=True))

