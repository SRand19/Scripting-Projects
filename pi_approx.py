iterations = int(input("How many iterations of pi would you like to calculate: "))
def estimate_pi(terms):
    result = 0.0
    for x in range(terms):
        result += (-1.0)**x/(2.0*x+1.0)
    return 4*result

print("PI = ", estimate_pi(iterations))
