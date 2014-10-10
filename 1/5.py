from prime import is_prime
def prime_number_of_divisors(n):
	number=1
	count=0
	while number != n+1:
		if n%number==0:
			count+=1
		number+=1
	return count
print (is_prime(prime_number_of_divisors(8)))

