def find_largest_and_smallest(numbers):
    if not numbers:
        return "The list is empty."

    largest = max(numbers)
    smallest = min(numbers)

    return largest, smallest

try:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    if numbers:
        largest, smallest = find_largest_and_smallest(numbers)
        print("Largest element:", largest)
        print("Smallest element:", smallest)
    else:
        print("The list is empty. Please enter valid numbers.")
except ValueError:
    print("Invalid input. Please enter only numbers separated by spaces.")
