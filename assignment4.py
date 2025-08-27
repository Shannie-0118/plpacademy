# Combined File Read, Modify & Write with Error Handling

filename = input("Enter the filename to read: ")

try:
    # Read the original file
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()
    
    # Prepare a new filename
    new_filename = f"modified_{filename}"
    
    # Write the modified content to the new file
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Success! Modified content written to '{new_filename}'.")
    
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' cannot be read or written.")
