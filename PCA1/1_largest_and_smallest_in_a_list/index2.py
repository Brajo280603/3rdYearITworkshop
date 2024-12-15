def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None

    largest = max(numbers)
    smallest = min(numbers)

    return largest, smallest

user_input = input("Enter numbers separated by spaces: ")

try:
    numbers = [int(num) for num in user_input.split()]  
    if numbers:  
        largest, smallest = find_largest_and_smallest(numbers)
        print(f"Largest element: {largest}")
        print(f"Smallest element: {smallest}")
    else:
        print("The list is empty. Please enter some numbers.")
except ValueError:
    print("Error: Please enter valid integers separated by spaces.")
