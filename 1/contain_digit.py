def contains_digit(number, digit):
	while number!=0:
		if number%10 == digit:
			return True
		else:
			number//=10
	
	return False
#print (contains_digit(423,5))