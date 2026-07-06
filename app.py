from flask import Flask, request, jsonify, render_template
import joblib

# Load the trained model
model = joblib.load('iris_model.pkl')

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # Render the HTML interface template
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json 
    features = data['features']
    prediction = model.predict([features]).tolist()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    app.run(host='0.0.0.0', port=5000, debug=False)