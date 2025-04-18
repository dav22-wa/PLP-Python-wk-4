# PLP-Python-wk-4

File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
Outcomes 🎉

By the end of this module, you’ll be skilled in managing files efficiently in Python, ensuring error-free code that gracefully handles unexpected issues. Mastering files and exception handling will allow you to build strong, robust applications!



def modify(text):
    return text.upper()

def main():
    filename = input("Filename to read: ")

    try:
        with open(filename, 'r') as f:
            data = f.read()
        updated = modify(data)
        with open("modified_" + filename, 'w') as f:
            f.write(updated)
        print("File saved as modified_" + filename)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("File can't be read or written.")

main()
