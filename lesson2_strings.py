first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print("Full name", full_name)

# String methods
print("\n--- String Methods ---")
message = " Hello, Python World!"
print("Original:", message)
print("Lowercase:", message.lower())
print("Tital case:", message.title())
print("Stripped (no spaces)", message.strip())
print("Length", len(message))

# String formatting
print("\n--- String Formatting ---")
age = 25
city = "New York"
# Method 1: fstrings (recommended)
print(f"I am {age} years old and live in {city}")

# Method 2: .format()
print("I am {} years old and i live in {}".format(age, city))

# Method 3: % operator (older style)
print( "I am %d years old and live in %s" % (age, city))

# String slicing
text = "Python Programming"
print("\n--- String Slicing ---")
print("Original", text)
print("First 6 characters:", text[0:6])
print("Last 11 characters:", text[-11:])
print("Every 2nd character:", text[::2])
print("Reverse:", text[::-1])