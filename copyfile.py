file1 = input("Enter the name of the first file: ")
file2 = input("Enter the second files name: ")

with open(file1, 'r') as f:
    contents = f.read()

with open(file2, 'w') as f:
    f.write(contents)

print(f"Contents of {file1} have been copies to {file2}")
