import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load("model.pkl")
feature_columns = joblib.load("features.pkl")

# Example user input
user_input = {
    "brand": "Ford",
    "model_year": 2020,
    "milage": 35000,
    "fuel_type": "Gasoline"
}

# Create base input with all features = 0
input_data = dict.fromkeys(feature_columns, 0)

# Fill numeric values
input_data["model_year"] = user_input["model_year"]
input_data["milage"] = user_input["milage"]

# Fill brand
brand_col = "brand_" + user_input["brand"]
if brand_col in input_data:
    input_data[brand_col] = 1

# Fill fuel type
fuel_col = "fuel_type_" + user_input["fuel_type"]
if fuel_col in input_data:
    input_data[fuel_col] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict
predicted_price = model.predict(input_df)

print("Predicted Price: $", round(predicted_price[0], 2))