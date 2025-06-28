# Basic function
def greet(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))

#Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

# Function with mutiple return values
def get_name_and_age():
    return "Alice", 25

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# Lamda funciotions (anonymous functions)
square = lambda x: x**2
print("Square of 5:", square(5))

# Using Lambda with built-int functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x > 2, numbers))

print("Original:", numbers)
print("Squared:", squared)
print("Filtered (>2):", filtered)