height = int(input("Please input the drop height: "))
bounces = int(input("Please input the number of times the ball is allowed to bounce :"))
first = 0
second = 0
for i in range(bounces):
    second = first + first * 0.6
    first = height + height * 0.6
    
print("The distance traveled is", second, "units.")
