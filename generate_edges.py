import pandas as pd

data = pd.read_csv("column_filtered.csv")

nodes = pd.read_csv("nodes.csv")
country_to_id = dict(zip(nodes['Label'], nodes['Id']))

rows = []

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

new_df = pd.DataFrame(rows)

print(new_df)

new_df.to_csv("edges.csv", index=False)
