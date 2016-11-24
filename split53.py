'''
Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is the same, with these constraints: all the values that are multiple of 5 must be in one group, and all the values that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)
'''

def _split53(nums, group1, group2, index):
	if index >= len(nums):
		return group1 == group2
	else:
		case1 = False
		case2 = False
		case3 = False

		if nums[index] % 5 == 0:
			case1 = _split53(nums, group1 + nums[index], group2, index+1)
		elif nums[index] % 3 == 0:
			case2 = _split53(nums, group1, group2 + nums[index], index+1)
		else:
			case3 = _split53(nums, group1, group2, index+1)
		return case1 or case2 or case3

def split53(nums):
	return _split53(nums, 0, 0, 0)

print(split53([1, 1]))
print(split53([1, 1, 1]))
print(split53([2, 4, 2]))
print(split53([2, 2, 2, 1]))
print(split53([3, 3, 5, 1]))
print(split53([3, 5, 8]))
print(split53([2, 4, 6]))
print(split53([3, 5, 6, 10, 3, 3]))
