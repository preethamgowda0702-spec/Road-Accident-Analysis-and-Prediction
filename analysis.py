import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel(
    r"C:\Users\NISCHITH R PRAKASH\OneDrive\Documents\Road Accident Data.xlsx"
)

# Remove unnecessary column
df = df.drop("Accident_Index", axis=1)

# Fill missing values
df["Road_Surface_Conditions"] = df["Road_Surface_Conditions"].fillna("Unknown")
df["Road_Type"] = df["Road_Type"].fillna("Unknown")
df["Weather_Conditions"] = df["Weather_Conditions"].fillna("Unknown")
df["Carriageway_Hazards"] = df["Carriageway_Hazards"].fillna("None")

print("Missing Values:")
print(df.isnull().sum())

print("\nData cleaned successfully!")

# -----------------------------
# Graph 1: Accident Severity
# -----------------------------
plt.figure(figsize=(8, 5))

df["Accident_Severity"].value_counts().plot(kind="bar")

plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")

plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.close()

print("Saved: severity_distribution.png")

# -----------------------------
# Graph 2: Weather Conditions
# -----------------------------
plt.figure(figsize=(10, 5))

df["Weather_Conditions"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Weather Conditions")
plt.xlabel("Weather")
plt.ylabel("Number of Accidents")

plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.close()

print("Saved: weather_conditions.png")

# -----------------------------
# Graph 3: Vehicle Types
# -----------------------------
plt.figure(figsize=(10, 5))

df["Vehicle_Type"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Vehicle Types Involved")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Accidents")

plt.tight_layout()
plt.savefig("vehicle_types.png")
plt.close()

print("Saved: vehicle_types.png")

print("\nAll graphs generated successfully!")