'''
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line ( their positions are fixed), and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies given to the children.
'''

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