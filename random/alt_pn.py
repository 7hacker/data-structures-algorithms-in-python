'''
Take a list of positive and negative integers, and return a list with negative numbers on left and positive numbers on right while also mantaining the order of numbers in input list
'''
def alt_pn2(nums):
    #without extra space
    return


def update_ptr(p,nums):
    if nums[p] > 0:
        for i in xrange(p+1,len(nums)):
            if nums[i] > 0:
                return i
    else:
        for i in xrange(p+1, len(nums)):
            if nums[i] < 0:
                return i
    return None


def alt_pn(nums):
    #with extra space
    res = []
    count = 0
    
    p_ptr = None
    n_ptr = None
    for i in xrange(len(nums)):
        if nums[i] > 0:
            p_ptr = i
            break
    for i in xrange(len(nums)):
        if nums[i] < 0:
            n_ptr = i
            break

    while count < len(nums):
        if p_ptr and count % 2 == 0:
            res.append(nums[count])
            p_ptr = update_ptr(p_ptr, nums)
        elif n_ptr:
            res.append(nums[count])
            n_ptr = update_ptr(n_ptr, nums)
        count = count + 1
    return res


print(alt_pn([2, 3, -4, -9, -1, -7, 1, -5, -6]))