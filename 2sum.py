'''
Given an array of integers, find two numbers such that they add up to a specific target number.
'''

def sum2(a, target):
    d = {}
    i = 0
    res = []

    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = i
    for i in range(len(a)):
        if target-a[i] in d and target-a[i] > a[i]:
            res.append((a[i], target-a[i]))
    return res

print(sum2([2,7,11,15, 3, 6], 9))