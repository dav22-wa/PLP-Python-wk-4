def modify_content(text):
    # Example modification: convert text to uppercase
    return text.upper()

def read_and_modify_file():
    filename = input("Enter the filename to read from: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        modified_content = modify_content(content)
        
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully.")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to the file.")

# Run the program
read_and_modify_file()
