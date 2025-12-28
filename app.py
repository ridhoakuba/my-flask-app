from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model & scaler
model = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    frekuensi = float(data["frekuensi"])
    rata_pengeluaran = float(data["rata_pengeluaran"])
    jarak = float(data["jarak"])

    # Buat array fitur
    fitur = np.array([[frekuensi, rata_pengeluaran, jarak]])

    # 🔥 WAJIB: scaling dulu sebelum prediksi!
    fitur_scaled = scaler.transform(fitur)

    # Prediksi
    prediksi = model.predict(fitur_scaled)[0]

    return jsonify({"hasil": prediksi})

if __name__ == "__main__":
    app.run(debug=True)
