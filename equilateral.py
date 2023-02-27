def is_equilateral(a, b, c):
    if a == b == c:
        return True
    else:
        return False

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if is_equilateral(a, b, c):
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
