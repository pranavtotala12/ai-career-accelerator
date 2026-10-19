import json

d= {
    "customer":"Pranav",
    "amount":800,
    "city":"Pune"
}

text = json.dumps(d)          #convert dic is json
print(text)
print(type(text))             #<class 'str'>

back = json.loads(text)       #json is dic
print(back["city"])

print(type(back))             #<class 'dict'>

print("------------")

response_data = {
 "answer": "An API lets applications communicate.",
 "success": True
}

json_text = json.dumps(response_data, indent=2)   #indent=2 for pretty print (to add spaces)
print(json_text)