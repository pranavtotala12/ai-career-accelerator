User = {
    "Name":"Pranav",
    "Age":"25",
    "Skills":"AI,Python"
}
print(User["Name"])
print(User.get("Phone"))   #use get for Safe side if key is missing it give None

print("-------------------------")

User["Gender"]="Male"      #To adding new "Key":"Value"
print(User)  
User["Phone"]="9359**7550"
print(User)  

print("-------------------------")

User.pop("Phone")          #To delete item from dict
print(User)

print("-------------------------")

User["Age"] = 9359647550   #To Update the Value
print(User)

print("-------------------------")

for i in User:             #Printing Items
    print(i," - ",User[i])

print("-------------------------")

print(User.items());




