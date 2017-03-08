'''
Binary Search!
'''
def binary_search(nums, target):
    #binary search to look for target in sorted nums
    start = 0
    end = len(nums) - 1
    mid = end / 2

    while start <= end:
        #print("Start: " + str(nums[start]))
        #print("End: " + str(nums[end]))
        #print("Mid: " + str(nums[mid]))

        if target == nums[mid]:
            print("Found! at : " + str(mid))
            return
        elif target > nums[mid]:
            start = mid+1
            mid = ( end + start ) / 2
        else: 
            end = mid -1
            mid = (end + start) / 2
    print("not found :(")
    return

binary_search([100,200,5000,3,5,8,9,11], 5000)
