import requests

url = 'http://127.0.0.1:5000/predict' # Switched to explicit local IP
data = {'features': [5.1, 3.5, 1.4, 0.2]}

try:
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Raw Response Text:", response.text)
except Exception as e:
    print("Connection Error:", e)