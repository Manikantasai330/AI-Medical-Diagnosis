AI-Powered Medical Diagnosis System
📌 Overview
This project is an AI-driven medical diagnosis system that detects pneumonia from chest X-ray images using Deep Learning (CNNs). It provides a FastAPI-based backend for real-time predictions and is Dockerized for easy deployment.

🚀 Features
✅ Deep Learning Model (CNN) trained on medical images
✅ FastAPI Backend for real-time predictions
✅ Supports Image Uploads via API
✅ Dockerized for smooth deployment

📂 Project Structure

AI-Medical-Diagnosis/
│── dataset/                  # Medical images dataset (Chest X-rays)
│── model/                    # Trained Deep Learning model
│── src/
│   ├── train.py              # CNN model training script
│── api/
│   ├── main.py               # FastAPI server for predictions
│── Dockerfile                # Containerization for easy deployment
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
🛠 Tech Stack
Python (Deep Learning & API)
TensorFlow/Keras (CNN Model)
FastAPI (Backend API)
Docker (Deployment)
🖼 How It Works
1️⃣ Train the Model:

python src/train.py
2️⃣ Run FastAPI Server:

uvicorn api.main:app --reload
3️⃣ Test the API (Using cURL or Postman):

curl -X 'POST' 'http://127.0.0.1:8000/predict/' -F 'file=@chest_xray.jpg'
🔗 Deployment Using Docker
To run this project inside a Docker container, use:

docker build -t ai-medical-diagnosis .
docker run -p 8000:8000 ai-medical-diagnosis
📜 License
This project is open-source and available under the MIT License.
