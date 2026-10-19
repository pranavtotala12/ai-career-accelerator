import json
request_data = {
    "question": "Explain REST API",
    "user":"Pranav",
    "max tokens": 200
}

print(request_data)
print(request_data["question"])

print("------------")

Question=request_data["question"].strip()  #remove extra spaces
user=request_data.get("user","Guest")
print(Question)
print(user)

print("------------")

Question=request_data["question"].strip()  #remove extra spaces

if Question =="":
    print("Question cant be empty")
else:
    print("Valid Question :",Question)

print("------------")

# List of Dictionaries
messages = [
    {"role":"system","content":"You are a helpful assistant."},
    {"role":"user","content":"Explain REST API"}
]

for message in messages:
    print(message["role"],":",message["content"])

print("------------")


response_data = {
 "answer": "An API lets applications communicate.",
 "success": True
}

json_text = json.dumps(response_data, indent=2)   #indent=2 for pretty print (to add spaces)
print(json_text)