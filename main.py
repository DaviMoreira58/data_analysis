import pandas as pd
import os

source = os.path.abspath('.')
db_file = os.path.join(source, 'cancelamentos.csv')

table = pd.read_csv(db_file)

table = table.drop(columns='CustomerID')

print(table.info())

table = table.dropna()

print(table.info())


