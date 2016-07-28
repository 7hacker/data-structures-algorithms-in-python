def alt_pn2(nums):
    #without extra space
    return


def alt_pn(nums):
    #with extra space
    res = list()
    pi = 0
    ni = 0
    positiveTurn = True
    
    while pi < len(nums) and ni < len(nums):
        while pi <len(nums) and nums[pi] < 0:
            pi = pi + 1
        while ni < len(nums) and nums[ni] > 0:
            ni = ni + 1
        if positiveTurn:
            print("Adding: " + str(nums[pi]))
            res.append(nums[pi])
            pi = pi + 1
            positiveTurn = False
        else:
            print("Adding: " + str(nums[ni]))
            res.append(nums[ni])
            ni = ni + 1
            positiveTurn = True
    
    if pi < len(nums):
        while pi < len(nums):
            pi = pi + 1
            res.append(nums[pi])
    if ni < len(nums):
        while ni < len(nums):
            ni = ni + 1
            res.append(nums[ni])

    print(res)

    return


print(alt_pn([2, 3, -4, -9, -1, -7, 1, -5, -6]))