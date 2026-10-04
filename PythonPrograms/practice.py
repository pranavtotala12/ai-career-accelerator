def create_message(name):
    return f"Hello, {name}! Welcome to the AI Career Accelerator."

print(create_message("Pranav"))

def divide_numbers(i):
    try:
        result = 10 / i
        return result
    except:
        print("Error: Division by zero is not allowed.")


print (divide_numbers(0))
