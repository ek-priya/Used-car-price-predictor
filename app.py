from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
feature_columns = joblib.load("features.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = dict.fromkeys(feature_columns, 0)

    input_data["model_year"] = int(data["model_year"])
    input_data["milage"] = int(data["milage"])

    brand_col = "brand_" + data["brand"]
    if brand_col in input_data:
        input_data[brand_col] = 1

    fuel_col = "fuel_type_" + data["fuel_type"]
    if fuel_col in input_data:
        input_data[fuel_col] = 1

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    return jsonify({
        "predicted_price": round(float(prediction), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)