'''
http://articles.leetcode.com/sliding-window-maximum
'''
def sliding_window_max(nums, w):
    result = [] #result stored here
    dq = [] #push and pop from front and end both. front will hold max
    #build the window at first
    dq.append(0)
    for i in xrange(1,w):
        while len(dq) and nums[i] > dq[-1]:
            dq.pop(-1)
        dq.append(i)
    #add the first max to the result array
    result.append(nums[dq[0]])

    #slide the window
    for i in range(w, len(nums)):
        #add an item into the window: but we are interested only in valid entries
        while len(dq) and nums[i] > dq[-1]:
            dq.pop(-1)
        dq.append(i)
        #the front of the window must be in range
        while len(dq) and i - dq[0] >= w:
            dq.pop(0)
        #result is now at front of queue
        result.append(nums[dq[0]])
    print(result)


nums = [1, 3, -1, -3, 5, 3, 6, 7]
w = 3
sliding_window_max(nums, w)