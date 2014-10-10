def sum_of_divisors(n):
	number=1
	sum=0
	while number != n+1:
		if n%number==0:
			sum+=number
		number+=1
	return sum
print (sum_of_divisors(1000)) 