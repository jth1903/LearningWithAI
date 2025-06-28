# If statements
print("--- If Statements ---")
age = 18

if age >= 18:
    print("Your are an adult")
elif age >= 13:
    print("Your are a teenager")
else:
    print("Your are a child")

# Comparison operators
print("\n--- Comparison Operators ---")
x = 10
y = 5

print("x > y", x > y) # Greater than
print("x <y:", x < y) # Less than
print("x == y:", x == y) # Equal to
print("x != y:", x != y) # Not equal to
print("x <= y:", x >= y) # Greater than or equal
print("x <= y:", x <= y) # Less than or equal

# Loops
print("\n--- For Loops ---")
# Loop trough a range
for i in range(5):
    print(f"Count: {i}")

# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loops
print("\n--- Whle Loops ---")
count = 0
while count < 3:
    print(f"While loop count: {count}")
    count += 1


# Break and continue
print("\n--- Break and Continue ---")
for i in range(10):
    if i == 3:
        continue # Skip 3
    if i == 7:
        break
    print(f"Number: {i}")