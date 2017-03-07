#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.25%)
# Total Accepted:    190184
# Total Submissions: 894832
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# [-1, 0, 1],
# [-1, -1, 2]
# ]
# 
#
class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        nums.sort()
        for i in xrange(0, len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                j = i + 1
                k = len(nums)-1
                while j < k :
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        j = j + 1
                        k = k - 1
                        while j < k and nums[j] == nums[j-1]:
                            j = j + 1
                        while j < k and nums[k] == nums[k+1]:
                            k = k - 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k = k -1
                    else:
                        j = j + 1
        return result
