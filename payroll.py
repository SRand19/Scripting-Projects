filename = input("Enter the name of the file: ")

with open(filename, 'r') as f:
    lines = f.readlines()

print(f"{'Name':<10}{'Hours':<10}{'Wages':<10}")

for line in lines:
    values = line.split()
    lastName = values[0]
    hourly = float(values[1])
    timeWorked = float(values[2])

    income = hourly * timeWorked

    print(f"{lastName:<10}{timeWorked:<10.2f}${income:<10.2f}")
