nums = input("input 4 numbers separated by commas : ")

nums = [int(num) for num in nums.split(",")]

nums.sort()

print("the smallest number is : " + str(nums[0]))
print("the largest number is : " + str(nums[-1]))



