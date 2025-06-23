# Writing to a file
print("--- File Handling---")

# Writing text to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file!\n")
    file.write("This is the second line.\n")
    file.write("And this is the third line.")

print("File written successfully!")

# Reading from a file
print("\n--- Reading File ---")
with open("sample.txt","r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nFile append successfully!")
