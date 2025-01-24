import pandas as pd

data = pd.read_csv("./row_filtered.csv", index_col=0)

columns_to_keep = ['reporterCode', 'flowCode', 'partnerCode', 'primaryValue']

filtered_data = data[columns_to_keep]

filtered_data.to_csv("column_filtered.csv", index=False)
