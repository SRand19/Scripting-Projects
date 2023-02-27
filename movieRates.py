newAmount = int(input("Please input the number of movies that are new: "))
oldieAmount = int(input("Please input the number of movies that are oldies: "))
duration = int(input("How many nights will you be renting these movies? "))
newRate = newAmount * 3 * duration
oldieRate = oldieAmount * 2 * duration
total = newRate + oldieRate
print("Your estinated total is $", total)

