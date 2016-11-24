'''
for an input array [1,2,3] return back an array where each i is a product of elements before i and after i, excluding i. In this example the output is: [6, 3, 2]
'''

def array_product(nums):
    result = [1] * len(nums)
    #going forward
    i = 0
    j = 1
    rolling = 1
    while j < len(result):
        rolling = rolling * nums[i]
        result[j] = result[j] * rolling
        i = i + 1
        j = j + 1

    print result

    #going backward
    i = len(nums)-1
    j = len(nums)-2
    rolling = 1
    while j > -1:
        rolling = rolling * nums[i]
        result[j] = result[j] * rolling
        i = i -1
        j = j -1 

    print result
    return

array_product([1,2,3,4,5])