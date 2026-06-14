import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("dataset/used_cars.csv")

# -------------------------
# Data Cleaning
# -------------------------

# Clean price
df["price"] = (
    df["price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Clean mileage
df["milage"] = (
    df["milage"]
    .str.replace(" mi.", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(int)
)

# Handle missing values
df["fuel_type"] = df["fuel_type"].fillna("Unknown")
df["accident"] = df["accident"].fillna("Unknown")
df["clean_title"] = df["clean_title"].fillna("Unknown")

# Keep only useful columns
df = df[
    [
        "brand",
        "model_year",
        "milage",
        "fuel_type",
        "price"
    ]
]

# Convert categorical columns to numeric
df = pd.get_dummies(df, columns=["brand", "fuel_type"])

# Separate features and target
X = df.drop("price", axis=1)
y = df["price"]

# Save feature names (important for prediction)
feature_columns = X.columns.tolist()
joblib.dump(feature_columns, "features.pkl")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
score = r2_score(y_test, predictions)

print("R2 Score:", score)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")