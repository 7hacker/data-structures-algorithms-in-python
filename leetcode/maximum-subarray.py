#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray
#
# Easy (39.02%)
# Total Accepted:    173753
# Total Submissions: 445238
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        max_so_far = -sys.maxint-1
        max_ending_here = 0
        for i in xrange(len(nums)):
        	max_ending_here = max_ending_here + nums[i]
        	if max_ending_here > max_so_far:
        		max_so_far = max_ending_here
        	if max_ending_here < 0:
        		max_ending_here = 0
        return max_so_far


