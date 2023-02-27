import math

def guess_number(lower, upper):
    guess = (lower + upper) // 2
    return guess

lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

max_guesses = int(math.ceil(math.log(upper - lower + 1, 2)))

print("Think of a number between", lower, "and", upper, ".")
print("I will try to guess it in at most", max_guesses, "guesses.")

for i in range(max_guesses):
    guess = guess_number(lower, upper)
    response = input("Is your number ", + str(guess) + "? (low/high/correct): ")
    if response == 'correct':
        print("Yay! I got it in", i + 1, "guesses.")
        break
    elif response == 'low':
        lower = guess + 1
    elif response == 'high':
        upper = guess - 1
    else:
        print("Error: please enter low, high, or correct.")

else:
    print("You cheated! The number was", guess)
