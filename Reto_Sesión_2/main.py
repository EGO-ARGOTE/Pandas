import pandas as pd

path = 'League_of_legend_Champions_2024.csv'

retail_data = pd.read_csv(path, encoding='latin1')

print(type(retail_data))

print(retail_data)