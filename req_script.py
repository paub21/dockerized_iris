import requests

#url = "http://172.26.112.1:5000/predict"  # Replace <host-ip> with the host's IP
url = "http://192.168.1.49:5000/predict"  # Replace <host-ip> with the host's IP
payload = {"features": [5.1, 3.5, 1.4, 0.2]}  # Example features : Setosa
payload = {"features": [6.0, 2.2, 4.0, 1.0]} # Example features : Versicolor
#payload = {"features": [6.9, 3.1, 5.4, 2.1]} # Example features : Verginica

response = requests.post(url, json=payload)
result = response.json()  # Convert response to a dictionary

if response.status_code == 200:
    print("Prediction:", response.json())  # Expected: {"prediction": "setosa"}
    print("Prediction Only:", result['prediction'])  # Access only the prediction
else:
    print("Error:", response.status_code, response.text)
    
    
