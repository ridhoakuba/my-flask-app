import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# === 1. Load Dataset ===
df = pd.read_csv("data/dataset_100.csv")

# Pisahkan fitur & label
X = df[["frekuensi", "rata_pengeluaran", "jarak"]]
y = df["label"]

# === 2. Scaling (WAJIB UNTUK KNN!) ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === 3. Train Test Split ===
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# === 4. KNN Model ===
model = KNeighborsClassifier(n_neighbors=3)


model.fit(X_train, y_train)

# === 5. Simpan model & scaler ===
joblib.dump(model, "knn_model.pkl")
joblib.dump(scaler, "scaler.pkl")

# === 6. Akurasi ===
print("Akurasi:", model.score(X_test, y_test))
