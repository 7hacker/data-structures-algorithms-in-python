'''
https://leetcode.com/problems/interleaving-string
'''
class Solution(object):

    def _isInterleave(self,s1, s2, i, j, match, n):
        if n == len(match):
            return True
        a = False
        b = False
        if i < len(s1) and s1[i] == match[n]:
            a = self._isInterleave(s1, s2, i+1, j, match, n+1)
        if j < len(s2) and s2[j] == match[n]:
            b = self._isInterleave(s1, s2, i, j+1, match, n+1)
        return a or b

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self._isInterleave(s1, s2, 0, 0, s3, 0)


s = Solution()
print "PASSED" if not s.isInterleave("a", "b", "a") else "FAILED" 
print "PASSED" if s.isInterleave("aa", "ab", "aaba") else "FAILED"
