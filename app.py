from flask import Flask, request, jsonify
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open("iris_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Class names from the Iris dataset
class_names = ["setosa", "versicolor", "virginica"]

@app.route("/", methods=["GET"])
def home():
    return "Iris Model API is running. Use the '/predict' endpoint to make predictions."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract input data from the request
        data = request.get_json()
        features = data.get("features")

        # Validate input
        if not isinstance(features, list) or len(features) != 4:
            return jsonify({"error": "Invalid input format. 'features' must be a list of 4 numbers."}), 400

        # Make a prediction
        prediction = model.predict([features])
        predicted_class = class_names[int(prediction[0])]

        # Return the result
        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
