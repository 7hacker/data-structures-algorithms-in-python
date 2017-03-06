def sumExists(a, target):
	start = 0
	end = 1
	target_check = a[start]
	
	while end < len(a):
		if target_check == target:
			print "Found! " + str(start) + "," + str(end) 
			return True
		elif target_check > target:
			target_check = target_check - a[start]
			start = start + 1
			while target_check > target:
				target_check = target_check - a[start]
				start = start + 1
		end = end + 1
		target_check = target_check + a[end]


	if target_check == target:
			print "Found! " + str(start) + "," + str(end) 
			return True

	while start != end:
		target_check = target_check - a[start]
		start = start + 1
		if target_check == target:
			print "Found! " + str(start) + "," + str(end) 
			return True


	return False

print sumExists([2, 7, 4, 9, 1, 3, 5], 2)
print sumExists([5, 1, 2, -3, 7, -4], 0)
