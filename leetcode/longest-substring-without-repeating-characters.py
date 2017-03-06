"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

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
        
