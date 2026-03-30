import requests

url = "http://127.0.0.1:5000/analyze"

data = {
    "resume_text": "I know Python and Machine Learning"
}

response = requests.post(url, json=data)

print(response.json())