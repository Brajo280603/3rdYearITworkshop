number = int(input("enter the number : "))
factorial = 1
temp_num = number
while temp_num > 1 :
    factorial = factorial * temp_num
    temp_num-=1

print(factorial)
