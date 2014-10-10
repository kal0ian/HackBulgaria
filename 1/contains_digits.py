from contain_digit import contains_digit
def contains_digits(number, digits):
	for i in digits:
		if contains_digit(number,i)==False:
			return False
	return True
print (contains_digits(402123, [0, 7, 4]))