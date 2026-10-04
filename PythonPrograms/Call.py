import requests

url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url, timeout=10)

print(r.status_code) # 200
print(r.json())
print(type(r))