import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load Dataset
df = pd.read_excel(
    r"C:\Users\NISCHITH R PRAKASH\OneDrive\Documents\Road Accident Data.xlsx"
)

# Use a sample to reduce training time and model size
df = df.sample(n=50000, random_state=42)

# Remove unnecessary column
df = df.drop("Accident_Index", axis=1)

# Fill missing values
df["Road_Surface_Conditions"] = df["Road_Surface_Conditions"].fillna("Unknown")
df["Road_Type"] = df["Road_Type"].fillna("Unknown")
df["Weather_Conditions"] = df["Weather_Conditions"].fillna("Unknown")
df["Carriageway_Hazards"] = df["Carriageway_Hazards"].fillna("None")
df["Time"] = df["Time"].fillna("00:00")

# Encode categorical columns
for col in df.columns:
    if df[col].dtype == "object" or str(df[col].dtype) == "str":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

# Features and Target
X = df.drop("Accident_Severity", axis=1)
y = df["Accident_Severity"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Smaller Random Forest
model = RandomForestClassifier(
    n_estimators=20,
    max_depth=10,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save compressed model
joblib.dump(
    model,
    "accident_model.joblib",
    compress=3
)

print("Model saved successfully!")