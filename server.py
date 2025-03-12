from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS to avoid CORS issues
import pickle
import numpy as np
import os

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get base directory

# Load model, scaler, and label encoder
with open(os.path.join(BASE_DIR, "fish_species_logreg.pkl"), "rb") as model_file:
    model = pickle.load(model_file)
with open(os.path.join(BASE_DIR, "scaler.pkl"), "rb") as scaler_file:
    scaler = pickle.load(scaler_file)
with open(os.path.join(BASE_DIR, "label_encoder.pkl"), "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

app = Flask(__name__, template_folder="templates")  # Set template folder
CORS(app)  # Enable CORS to allow frontend to connect

@app.route('/')
def home():
    return render_template("index.html")  # Serve HTML page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)
        species = label_encoder.inverse_transform(prediction)[0]
        return jsonify({"species": species})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
