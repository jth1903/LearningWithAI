# Lists - ordered, changeable collections
print("--- Lists ---")
fruits = ["apple", "banana", "orange"]
print("Original list:", fruits)
 
# Adding elelments
fruits.append("grape")
fruits.insert(1, "mango")
print("After adding:", fruits)

# Removing elements
fruits.remove("banana")
popped_fruit = fruits.pop()
print("After removing", fruits)
print("Popped fruit:", popped_fruit)

# List operations
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)
print("Sum", sum(numbers))
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# List Comprehension
squares = [x**2 for x in numbers]
print("Squares:", squares)

# Tuples - ordered, immutable collections
print("\n--- Tuples ---")
coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X coordinates:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Dictionaries - key-value pairs
print("\n--- Dictionaries ---")
person = {
    "name": "John",
    "age": 30,
    "city":"New York",
    "hobbies": ["reading", "swimming"]
}

# Adding/updating dictionary
person["email"] = "john@example.com"
person["age"] = 31
print("Updating person:", person)

# Looping through dictionary
print("\n--- Looping through Dictionary ---")
for key, value in person.items():
    print(f"{key}: {value}")
