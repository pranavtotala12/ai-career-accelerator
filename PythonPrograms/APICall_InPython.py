import requests
try:
    url = "https://jsonplaceholder.typicode.com/todos/1"
    r = requests.get(url, timeout=10)
except Exception as e:
    print("Error: ",e)
else:
    print(r.status_code)
    print(r.json())