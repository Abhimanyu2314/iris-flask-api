from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load('iris_model.pkl')

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return 'Machine Learning Model Deployment with Flask'

@app.route('/predict', methods=['POST'])
def predict():
    # Receive data as JSON format
    data = request.json 
    features = data['features']
    
    # Format features as a nested list for the model and predict
    prediction = model.predict([features]).tolist()
    
    # Return the prediction back as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    # Upgrades for production deployment:
    # 1. debug=False ensures internal error tracking pages are hidden from public users.
    # 2. host='0.0.0.0' binds the server to all public IP addresses so external clients can access it.
    # 3. port=5000 sets the standard listening port.
    app.run(host='0.0.0.0', port=5000, debug=False)