def find_min_in_rotated_array(nums):
	start = 0
	end = len(nums) - 1
	mid = end / 2

	while start <= end:
		candidate = nums[mid]
		print("candidate: " + str(candidate))
		print("Start: " + str(nums[start]))
		print("End: " + str(nums[end]))

		if candidate < nums[mid-1] and candidate < nums[mid+1]:
			return candidate
		else:
			if nums[mid] < nums[start]:
				end = mid
				mid = (end + start)/2
			else:
				start = mid
				mid = (end + start)/2

	return None


def binary_search(nums, target):
	#binary search to look for target in sorted nums
	start = 0
	end = len(nums) - 1
	mid = end / 2

	while start <= end:
		print("Start: " + str(nums[start]))
		print("End: " + str(nums[end]))
		print("Mid: " + str(nums[mid]))

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

#binary_search([3,5,8,9,11,100,200,5000], 111)
print(find_min_in_rotated_array([100,200,5000,3,5,8,9,11]))
