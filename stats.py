def median(numbers):
    a = len(numbers)
    if a == 0:
        return 0
    sort = sorted(numbers)
    mid = a // 2
    if a % 2 == 0:
        return (sort[mid - 1] + sort[mid]) / 2
    else:
        return sort[mid]

def mode(numbers):
    if len(numbers) == 0:
        return 0
    counts = {}
    for b in numbers:
        counts[b] = counts.get(b, 0) + 1
    max_count = max(counts.values())
    modes = [b for b, count in counts.items() if count == max_count]
    if len(modes) == len(numbers):
        return None
    if len(modes) == 1:
        return modes[0]
    return min(modes)

def mean(numbers):
    c = len(numbers)
    if c ==0:
        return 0
    return sum(numbers) / c

def main():
    numbers_input = input("Enter the list of numbers seperated by commas please: ")
    numbers = [float(d) for d in numbers_input.split(',')]
    print(f"List of numbers: {numbers}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")
    print(f"Mean: {mean(numbers)}")
    
if __name__ == '__main__':
    main()
