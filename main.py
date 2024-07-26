import pandas as pd
import os

source = os.path.abspath('.')
db_file = os.path.join(source, 'cancelamentos.csv')

table = pd.read_csv(db_file)

