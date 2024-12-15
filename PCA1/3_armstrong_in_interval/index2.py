def is_armstrong(number):
    digits = str(number)  
    power = len(digits)   
    total = 0             
    for digit in digits:
        total += int(digit) ** power  
    return total == number

def find_armstrong_in_interval(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]

start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

armstrong_numbers = find_armstrong_in_interval(start, end)
if armstrong_numbers:
    print(f"Armstrong numbers in the interval [{start}, {end}]: {armstrong_numbers}")
else:
    print(f"No Armstrong numbers found in the interval [{start}, {end}].")
