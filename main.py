from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image

app = FastAPI()
model = tf.keras.models.load_model("model/pneumonia_model.h5")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).resize((150, 150))
    image = np.array(image) / 255.0
    image = image.reshape(1, 150, 150, 3)

    prediction = model.predict(image)[0][0]
    result = "Pneumonia Detected" if prediction > 0.5 else "Normal"

    return {"prediction": result, "confidence": float(prediction)}
