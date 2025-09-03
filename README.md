Iris Classifier API (FastAPI + scikit-learn)

A simple FastAPI-based machine learning API that predicts the species of an Iris flower using a trained RandomForestClassifier.

📂 Project Structure

project_root/
│
├── app/
│   ├── __init__.py        # (optional) marks app as a Python package
│   ├── main.py            # FastAPI app definition
│   └── schemas.py         # Pydantic models for input/output validation
│
├── model/
│   └── iris_model.joblib  # Trained ML model file
│
├── train_model.py         # Script to train and save the model
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

🚀 Getting Started

1️⃣ Create Virtual Environment

python -m venv env

Activate it:

Windows (cmd.exe):

env\Scripts\activate

Windows (PowerShell) (if scripts disabled, run Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass first):

.\env\Scripts\Activate.ps1

macOS/Linux:

source env/bin/activate

2️⃣ Install Dependencies

pip install -r requirements.txt

Example requirements.txt:

fastapi
uvicorn
scikit-learn
joblib
numpy

3️⃣ Train Model

python train_model.py

This will create model/iris_model.joblib.

4️⃣ Run API

uvicorn app.main:app --reload

The API will be available at: http://127.0.0.1:8000

![alt text](<image.png>)

📡 API Endpoints

Health Check

GET /health

{"status": "API is running"}

Model Info

GET /info

{
  "model_type": "RandomForestClassifier",
  "classes": ["setosa", "versicolor", "virginica"]
}

Predict Species

POST /predict
Request Body:

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Response:

{
  "predicted_class": "setosa"
}

📖 Interactive Docs

FastAPI provides built-in Swagger UI at:

http://127.0.0.1:8000/docs

🛠 Troubleshooting

404 Not Found on / → The root path / is not defined. Use /health, /info, or /predict.

FileNotFoundError: iris_model.joblib → Run train_model.py to generate the model.

PowerShell script execution disabled → Run Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass in PowerShell.

📜 License

This project is for educational purposes.