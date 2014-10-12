def is_prime(n):
	number=1
	count=0
	while number!=n+1:
		if n%number==0 :
			count+=1
		number+=1
	if count==2:
		return True
	else: return False
#print (is_prime(11))