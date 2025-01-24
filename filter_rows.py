import pandas as pd
from m49_cn import m49_cn

data = pd.read_csv("./data.csv", index_col=0)

columns_to_replace = ['reporterCode', 'partnerCode', 'partner2Code']

for column in columns_to_replace:
    if column in data.columns:
        data[column] = data[column].apply(lambda code: m49_cn.get(code, None))

filtered_data = data.dropna(subset=['reporterCode', 'partnerCode'])

filtered_data.reset_index(drop=True, inplace=True)

filtered_data.to_csv("row_filtered.csv")
