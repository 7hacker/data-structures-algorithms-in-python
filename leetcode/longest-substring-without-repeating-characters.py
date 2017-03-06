#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Medium (23.92%)
# Total Accepted:    258414
# Total Submissions: 1080468
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        end = 0
        u = set()
        while end < len(s):
        	if s[end] not in u:
        		u.add(s[end])
        		end = end + 1
        	else:
        		res = max(res, len(u))
        		while s[end] in u:
        			u.remove(s[start])
        			start = start + 1
        		u.add(s[end])
        		end = end + 1
        res = max(res, len(u))
        return res

t = Solution()
print t.lengthOfLongestSubstring("abcabcbb")
print t.lengthOfLongestSubstring("bbbbb")
print t.lengthOfLongestSubstring("pwwkew")
print t.lengthOfLongestSubstring("c")
print t.lengthOfLongestSubstring("dvdf")
