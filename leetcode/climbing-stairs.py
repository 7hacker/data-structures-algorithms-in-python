#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs
#
# Easy (39.01%)
# Total Accepted:    158265
# Total Submissions: 405666
# Testcase Example:  '1'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stairs = [0, 1, 2]
        if n > 2:
            for i in xrange(3,n+1):
                stairs.append(stairs[i-1] + stairs[i-2])
            return stairs[n]
        else:
            return stairs[n]
        
