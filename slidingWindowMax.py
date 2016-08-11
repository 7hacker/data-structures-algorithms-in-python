'''
http://articles.leetcode.com/sliding-window-maximum
'''
def sliding_window_max(nums, w):
	swl = []
	q = []
	for i in range(w):
		q.append(nums[i])
	cmax = max(q)
	swl.append(cmax)

	for i in range(w, len(nums)):
		out = q.pop(0)
		q.append(nums[i])
		if out != cmax and q[-1] <= cmax:
			#cmax stays the same
			swl.append(cmax)
		elif q[-1] > cmax:
			#cmax has changed and is the new entry
			cmax = q[-1]
			swl.append(cmax)
		else:
			#a new cmax needs to be computed
			cmax = max(q)
			swl.append(cmax)
		
	return swl

nums = [1, 3, -1, -3, 5, 3, 6, 7]
w = 3
print(sliding_window_max(nums, w))