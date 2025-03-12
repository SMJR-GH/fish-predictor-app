import requests

# Define the API URL
API_URL = "http://127.0.0.1:5000/predict"

# Corrected JSON format with 6 required features
data = {
    "features": [250.0, 23.2, 25.4, 30.0, 11.52, 4.02]  # Includes "Weight"
}

# Send a POST request to Flask API
response = requests.post(API_URL, json=data)

# Print the API response
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
