from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# -------------------------
# Load trained model
# -------------------------
model_path = "models/trained_model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)


# -------------------------
# Home Route
# -------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -------------------------
# Prediction Route
# -------------------------
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    input_data = pd.DataFrame([{
        "CodedDay": int(data["coded_day"]),
        "Zone": int(data["zone"]),
        "Weather": int(data["weather"]),
        "Temperature": int(data["temperature"])
    }])

    prediction = model.predict(input_data)[0]

    return jsonify({"Traffic_Prediction": prediction})


# -------------------------
# Run App
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
