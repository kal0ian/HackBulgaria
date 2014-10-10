def sevens_in_a_row(arr, n):
	count =0
	for number in arr:
		if number == 7:
			count+=1
		else: 
			count=0
		if count==n:
			return True
	return False
print (sevens_in_a_row([10,8,7,6,3,7,7,20,-7], 3))


