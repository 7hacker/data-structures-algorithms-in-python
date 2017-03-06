'''
Given a set of integers find a contiguous subset who sum is zero. There can be duplicates in the input
eg Input: 5, 1, 2, -3, 7, -4
Output: 1,2,-3 OR -3,7,-4
'''

def subZero(nums):
	h = {}
	s = 0
	for i in xrange(len(nums)):
		s = s + nums[i]
		if s in h:
			return nums[h[s]+1: i+1]
		else:
			h[s] = i
	return []


def getSum(a):
	s = 0
	for i in xrange(len(a)):
		s = s + a[i]
	return s


def allSubZero(nums):
	for i in xrange(len(nums)):
		selected = []
		for j in xrange(i, len(nums)):
			selected.append(nums[j])
			if getSum(selected) == 0:
				print selected


#print subZero([5,1,2,-3,7,-4])
allSubZero([5,1,2,-3,7,-4])
allSubZero([4, 2, -3, 1, 6])

#print subZero([4, 2, -3, 1, 6])
#print subZero([4, 2, 0, 1, 6])
#print subZero([-3, 2, 3, 1, 6])