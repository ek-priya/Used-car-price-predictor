# 🚗 Used Car Price Predictor

A full-stack Machine Learning web application that predicts the market value of a used car based on user inputs such as brand, manufacturing year, mileage, and fuel type.

## 📌 Project Overview

Buying or selling a used car often involves uncertainty in pricing. This project aims to solve that by using Machine Learning to estimate a fair market price based on historical car listing data.

Users can enter car details through a web interface, and the model predicts an estimated price instantly.

---

## ✨ Features

* Predict used car prices in real time
* User-friendly web interface
* Machine Learning-based prediction
* Flask backend API
* Attractive responsive UI with premium car-themed design
* End-to-end integration of Frontend + Backend + ML Model

---

## 🛠 Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Joblib

### Deployment

* GitHub
* Render

---

## 📂 Project Structure

```bash
Used-car-price-predictor/
│
├── app.py
├── train.py
├── predict.py
├── model.pkl
├── features.pkl
├── requirements.txt
│
├── dataset/
│   └── used_cars.csv
│
├── static/
│   ├── style.css
│   └── bg-car.jpg
│
└── templates/
    └── index.html
```

---

## ⚙ How It Works

### 1. Data Preprocessing

The dataset is cleaned by:

* Removing `$` and commas from price
* Cleaning mileage values
* Handling missing values
* Encoding categorical columns using one-hot encoding

### 2. Model Training

A **Random Forest Regressor** is trained using:

* Brand
* Model Year
* Mileage
* Fuel Type

### 3. Prediction

When a user enters car details:

1. Frontend sends input to Flask backend
2. Backend preprocesses input
3. Saved ML model predicts price
4. Predicted value is shown on screen

---

## 🔄 Application Flow

```text
User Input
   ↓
Frontend Form
   ↓
Flask API
   ↓
Preprocessing
   ↓
ML Model (Random Forest)
   ↓
Predicted Price
   ↓
Display Result
```

---

## 📊 Model Information

* Algorithm: Random Forest Regressor
* Dataset Size: 4000+ car records
* Evaluation Metric: R² Score

The model was trained to understand how:

* Older cars depreciate
* Higher mileage reduces value
* Brand affects resale price
* Fuel type influences pricing

---

## 🚀 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/ek-priya/Used-car-price-predictor.git
cd Used-car-price-predictor
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train.py
```

### Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

* Add more Indian car brands
* Improve prediction accuracy using more features
* Add transmission and engine specs
* Deploy live on cloud
* Add car image recommendations
* Support Indian Rupee pricing (₹)

---

## Learning Outcomes

Through this project, I learned:

* Data cleaning and preprocessing
* Machine Learning model training
* Model serialization using Joblib
* Flask API development
* Frontend–Backend integration
* Deployment workflow using GitHub and Render

---

## Author

**Keerthi Priya**
B.Tech Computer Science Engineering Student
Passionate about Full Stack Development, AI, and Problem Solving

---

⭐ If you found this project useful, feel free to star the repository.
