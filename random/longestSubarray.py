s = '''
74
659
931
273
545
879
924
710
441
166
493
43
988
504
328
730
841
613
304
170
710
158
561
934
100
279
817
336
98
827
513
268
811
634
980
150
580
822
968
673
394
337
486
746
229
92
195
358
2
154
709
945
669
491
125
197
531
904
723
667
550
'''

def maxSubarraySize(nums, target):
	target_copy = target
	window = 0
	start = 0
	while nums[start] > target:
		start = start + 1
	end = start

	while end < len(nums):
		target_copy = target_copy - nums[end]
		if target_copy > 0:
			end = end + 1
		else:
			window = max (window, (end-start))
			target_copy = target_copy + nums[start]
			start = start + 1
			end = end + 1





	return window


nums = []
for item in s.split():
	nums.append(int(item))
print nums
target = 22337
print maxSubarraySize(nums, target)



