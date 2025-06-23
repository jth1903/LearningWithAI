# Try-except blocks
print("--- Error Handlint ---")

# Basic error handling
try:
    number = int(input("Ente a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else: 
    print("No errors occurred!")
finally:
    print("This always runs!")

# Raising exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age {age} is valid"

# Testing the function
try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"Error: {e}")