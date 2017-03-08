'''
Given an unsorted array of nonnegative integers, is there a subarray which adds to a given number. 
'''
def sum_exists(a, t):
	start = 0
	end = 1
	k = t - a[start]
	if k == 0:
		return True
	while end < len(a):
		k = k - a[end]
		if k == 0:
			return True
		else:
			if k > 0:
				end = end + 1
			else:
				while k < 0:
					k = k + a[start]
					start = start + 1
				if k == 0:
					return True
				else:
					end = end + 1
	while start != end:
		k = k + a[start]
		start = start + 1
		if k == 0:
			return True
	return False

print sum_exists([1, 3, 5, 23, 2], 7)
