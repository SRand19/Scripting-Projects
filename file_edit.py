def main():
    filename = input("Enter the name of the file: ")
    with open(filename, 'r') as file:
        lines = file.readlines()

    while True:
        num_lines = len(lines)
        print(f"There are {num_lines} amount of lines in this file.")
        line_num = int(input("Enter a line number, or enter a 0 to exit."))
        if line_num == 0:
            break
        if line_num > 0 and line_num <= num_lines:
            line = lines[line_num - 1]
            print(line)
        else:
            print("Error: Invalid number, please try again.")

if __name__ == '__main__':
    main()
