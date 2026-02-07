filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("\nFile content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
