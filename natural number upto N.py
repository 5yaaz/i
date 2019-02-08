number=int(input())
if number < 0:
	print("")
else:	
	sum = 0
   	while(number > 0):
   		sum +=number
   		number -= 1
   	print(sum)
