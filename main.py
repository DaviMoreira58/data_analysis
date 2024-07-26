import pandas as pd
import os
import plotly.express as px

source = os.path.abspath('.')
db_file = os.path.join(source, 'cancelamentos.csv')

table = pd.read_csv(db_file)

table = table.drop(columns='CustomerID')

table = table.dropna()

for colum in table.columns:
    graphic = px.histogram(table, x=colum, color='cancelou')

filter = table['ligacoes_callcenter'] <= 4
table = table[filter] # 36%

filter = table['dias_atraso'] <= 20
table = table[filter] # 26%


