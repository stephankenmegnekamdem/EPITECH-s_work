def is_multiple_3(val):
    return val % 3  == 0

def is_multiple_5(val):
	return val % 5 == 0


i=-30
while i<=30:
	flag3 = 0
	flag5 = 0
	flagboth = 0
	if is_multiple_3(i):
		flag3=1
	if is_multiple_5(i):
		flag5=1
		if flag3==1:
			flagboth=1
	if flagboth==1 :
		print("FizzBuzz")
	else:
		if flag3==1:
			print("Fizz")
		else:
			if flag5==1:
				print("Buzz")
			else:
				print(i)

	i=i+1


