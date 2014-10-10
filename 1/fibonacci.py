def nth_fibonacci(n):
	fib1=1
	fib2=1
	if n==1 or n==2:
			print(fib1)
	else:
		while n!=2:
			buf=fib2
			fib2= fib2+fib1
			fib1=buf

			n-=1
		return fib2

print (nth_fibonacci(10))