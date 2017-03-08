'''
http://www.programcreek.com/2013/03/leetcode-palindrome-partitioning-java/
'''

def isPalindromeHelper(s, start, end):
    #is there a palindrome from start to end (inclusive)
    if start == end:
        return True
    i = start
    j = end
    while s[i] == s[j] and i <= j:
        i = i + 1
        j = j - 1
    if i < j:
        return False
    else:
        return True

def buildCache(s, cache):
    for i in xrange(len(cache)):
        for j in xrange(len(cache)):
            if i == j:
                cache[i][j] = 1
            elif i > j:
                cache[i][j] = -1
            else:
                if isPalindromeHelper(s, i, j):
                    cache[i][j] = 1
                else:
                    cache[i][j] = 0

def palindromeDecomposition(s, cache, i, result, resultList):
    if i >= len(s):
        if result not in resultList:
            resultList.append(result)
        return
    else:
        #cache[i][i] is always going to be 1
        k = 0
        while i+k < len(cache):
            if cache[i][i+k] == 1:
                palindromeDecomposition(s, cache, i+k+1, result+s[i:i+k+1]+"|", resultList)
            k = k + 1


s = "Neveroddoreven"
cache_size = len(s)
cache = [[None]*cache_size for i in xrange(cache_size)]
buildCache(s, cache)
resultList = []
palindromeDecomposition(s, cache, 0, "", resultList)
print(resultList)
