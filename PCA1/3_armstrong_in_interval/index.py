def is_armstrong(number):
    digits = list(map(int, str(number)))
    power = len(digits)
    return number == sum(d ** power for d in digits)

def find_armstrong_in_interval(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

armstrong_numbers = find_armstrong_in_interval(start, end)
if armstrong_numbers:
    print(f"Armstrong numbers in the interval [{start}, {end}]: {armstrong_numbers}")
else:
    print(f"No Armstrong numbers found in the interval [{start}, {end}].")
