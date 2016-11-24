'''
Given a sorted array and a number x, find the pair in array whose sum is closest to x
'''

import sys

def closestSumPair(a, t):
	diff = sys.maxint
	pair = (None, None)
	start = 0
	end = len(a)-1

	while start < end:
		newDiff = abs(t-(a[start] + a[end]))
		if newDiff < diff:
			diff = newDiff
			pair = (a[start], a[end])
		if (a[start] + a[end]) > t:
			end = end - 1
		else:
			start = start + 1

	return pair

print(closestSumPair([1, 3, 4, 7, 10], 15))
