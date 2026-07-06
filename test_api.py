import requests

# Your unique live URL from the Render dashboard
url = 'https://iris-flask-api-eax0.onrender.com/predict'

data = {'features': [5.1, 3.5, 1.4, 0.2]}

try:
    print("Sending data to your live cloud server...")
    response = requests.post(url, json=data)
    
    print("Status Code:", response.status_code)
    print("Live API Response:", response.json())
except Exception as e:
    print("An error occurred connecting to the cloud:", e)