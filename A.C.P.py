with open("operations.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("File Handling in Python is interesting!\n")

print("Step 1: File 'operations.txt' created and written successfully.\n")

with open("operations.txt", "r") as file:
    print("Step 2: Reading contents of 'operations.txt':")
    content = file.read()
    print(content)

with open("operations.txt", "a") as file:
    file.write("Appending another line to the file.\n")
    file.write("Learning Python is fun!\n")

print("\nStep 3: Data appended successfully.\n")

with open("operations.txt", "r") as file:
    print("Step 4: Updated file contents:")
    updated_content = file.read()
    print(updated_content)

print("\nStep 5: Reading file line by line:")
with open("operations.txt", "r") as file:
    for index, line in enumerate(file, start=1):
        print(f"Line {index}: {line.strip()}")
