import requests

result = requests.get("http://127.0.0.1:5000")
print(result.text)
