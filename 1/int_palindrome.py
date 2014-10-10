def is_int_palindrome(n):
	reverse=0
	buf=n
	while buf!=0:
		reverse *= 10
		reverse += buf%10
		buf//=10

	if n==reverse:
		return True
	else: return False
	
print(is_int_palindrome(121))
