import pandas as pd

# Load the dataset
data = pd.read_csv("column_filtered.csv")

nodes = pd.read_csv("nodes.csv")  # Country-to-ID mapping
country_to_id = dict(zip(nodes['Label'], nodes['Id']))

# Initialize an empty list to store rows for the new DataFrame
rows = []

# Iterate over each row in the dataset
for _, row in data.iterrows():
    source = None
    target = None
    if row['flowCode'] == "X" or row['flowCode'] == "DX" or row['flowCode'] == "RX":  # If flowCode is "X"
        source = country_to_id.get(row['reporterCode'])
        target = country_to_id.get(row['partnerCode'])
    elif row['flowCode'] == "M" or row['flowCode'] == "RM" or row['flowCode'] == "FM":  # If flowCode is "M"
        source = country_to_id.get(row['partnerCode'])
        target = country_to_id.get(row['reporterCode'])

    if source is not None and target is not None:
        rows.append({
            "Source": source,
            "Target": target,
            "Weight": row['primaryValue'],
            "Type": "directed"
        })

# Create the new DataFrame from the rows
new_df = pd.DataFrame(rows)

# Print the resulting DataFrame
print(new_df)

# Save the new DataFrame to a CSV file
new_df.to_csv("edges.csv", index=False)
