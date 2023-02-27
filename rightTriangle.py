def is_right(a, b, c):
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return True
    else:
        return False
    
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if is_right(a, b, c):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
