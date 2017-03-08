import sys

def rec_maxContiguousSum(a,i,rolling_sum,max_sum):
	if i >= len(a):
		if rolling_sum > max_sum:
			max_sum = rolling_sum
		return
	else:
		rec_maxContiguousSum(a, i+1, rolling_sum, max_sum)
		rec_maxContiguousSum(a, i+1, rolling_sum+a[i], max_sum)

max_sum = -sys.maxint-1
rec_maxContiguousSum([2, -1, 2, 3, 4, -5], 0, 0, max_sum)
print(max_sum)
