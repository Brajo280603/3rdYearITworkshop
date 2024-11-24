limit_num = int(input("enter the max range number : "))

prev_num = 0

current_num = 1

temp_current_num = 0

while current_num < limit_num:
	if (prev_num == 0):
		print(str(prev_num) + ", "+str(current_num))
	else:
		print(", "+str(current_num))
	temp_current_num = current_num
	current_num = current_num + prev_num
	prev_num = temp_current_num

