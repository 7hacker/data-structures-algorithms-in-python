def rec_candies(a):
	result = [0] * len(a)
	#find local minima and store in result table
	if a[0] < a[1]:
		result[0] = 1
	if a[-1] < a[-2]:
		result[-1] = 1
	i = 1
	while i < len(a)-1 :
		if a[i] < a[i-1] and a[i] < a[i+1]:
			result[i] = 1
			i = i + 2
		else:
			i = i + 1
	print(result)
	return 0


students = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
print(rec_candies(students))