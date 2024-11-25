start_index = int(input("enter first number of range : "))
end_index = int(input("enter the last number of range : "))


sum_of_squares = 0
for i in range(start_index,end_index+1):
	sum_of_squares = sum_of_squares + i**2

print("sum of squares in that range : " + str(sum_of_squares))

