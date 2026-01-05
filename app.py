from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load model once
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])

        prediction = model.predict([[area, bedrooms, bathrooms]])
        price = round(prediction[0], 2)

        return jsonify({"price": price})

    except:
        return jsonify({"error": "Invalid input"})

if __name__ == "__main__":
    app.run(debug=True)
