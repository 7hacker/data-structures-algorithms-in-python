'''
You are given the length of an array filled with all zeros initially. Now additions(updations) will be performed over given ranges on this array. Each updation will include the range and the number to be added over that range and will be of the form: [start index, end index, increment]. You have to return the final updated array after all the updations are done. Note: The time complexity should be O(n+k) where k is the number of updations and space complexity should be O(1) [https://discuss.leetcode.com/topic/224/range-addition]
'''

def kUpdates(a, k):
    n = len(a)
    for i in xrange(len(k)):
        startIndex = k[i][0]
        endIndex = k[i][1]
        inc = k[i][2]
        a[startIndex] = a[startIndex] + inc
        if endIndex+1 < n:
            a[endIndex+1] = a[endIndex+1] - inc

    for i in xrange(1,len(a)):
        a[i] = a[i] + a[i-1]
    return a

a = [0] * 5
print(a)
updates = [(1,3,2), (1,2,1), (2,4,-1)]
kUpdates(a, updates)
print(a)