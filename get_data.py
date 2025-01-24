import comtradeapicall
import pandas as pd

primary_key = "b0fd16b80b964a84abd09d19d0535f87"
secondary_key = "c64927444ac44bf3b1370ba84a827f85"

silicon = "280461"
chem_elems = "381800"
selenium = "280490"

data = comtradeapicall.getFinalData(
    subscription_key=primary_key,
    typeCode="C",
    freqCode="A",
    clCode="HS",
    period="2023",
    cmdCode=chem_elems,
    reporterCode=None,
    flowCode=None,
    partnerCode=None,
    partner2Code=None,
    customsCode=None,
    motCode=None
)

print(data)
print(data.shape)

data.to_csv("./data.csv")
