import pandas as pd
from m49_cn import m49_cn

data = pd.read_csv("./data.csv", index_col=0)

# List of columns to process
columns_to_replace = ['reporterCode', 'partnerCode', 'partner2Code']

# Replace values in the specified columns with country names or None
for column in columns_to_replace:
    if column in data.columns:
        data[column] = data[column].apply(lambda code: m49_cn.get(code, None))

# Filter out rows where any of the specified columns contain None
filtered_data = data.dropna(subset=['reporterCode', 'partnerCode'])

filtered_data.reset_index(drop=True, inplace=True)

# Print the filtered DataFrame
filtered_data.to_csv("row_filtered.csv")
