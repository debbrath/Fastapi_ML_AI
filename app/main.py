# app/main.py

from fastapi import FastAPI
from .schemas import IrisInput, PredictionOutput
import joblib
import numpy as np
import os


print("Current working directory:", os.getcwd())
print("Model path exists:", os.path.exists("model/iris_model.joblib"))

model = joblib.load("model/iris_model.joblib")

# Load the model once at startup
#model = joblib.load("../model/iris_model.joblib")

# Iris class names for readability
class_names = ['setosa', 'versicolor', 'virginica']

# Create FastAPI app
app = FastAPI(
    title="Iris Classifier API",
    description="API for predicting Iris species using FastAPI",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "API is running"}

@app.get("/info")
def model_info():
    """Basic model info"""
    return {
        "model_type": "RandomForestClassifier",
        "classes": class_names
    }

@app.post("/predict", response_model=PredictionOutput)
def predict_species(data: IrisInput):
    """Make prediction from input features"""
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    predicted_class = class_names[prediction]
    return {"predicted_class": predicted_class}



