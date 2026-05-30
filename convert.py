import pandas as pd

df = pd.read_excel(
    r"C:\Users\NISCHITH R PRAKASH\OneDrive\Documents\Road Accident Data.xlsx"
)

df.to_csv("road_accident_data.csv", index=False)

print("CSV created successfully!")