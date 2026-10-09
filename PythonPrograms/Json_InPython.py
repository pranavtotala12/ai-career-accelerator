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