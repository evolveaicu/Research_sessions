import requests

# Test API
response = requests.get("http://localhost:8000/")
print(response.json())
# Output: {'message': 'Hello Backend'}
