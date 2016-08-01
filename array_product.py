'''
array_product.py : for an input array [1,2,3] return back an array where each i is a product of elements before i and after i, excluding i. In this example the output is: [6, 3, 2]
'''

def array_product(nums):
	result = [0] * len(nums)
	#make the "after" products
	result[0] = 1
	count = 1
	for i in range(len(nums)-2, -1, -1):
		result[count] = result[count-1] * nums[i+1]
		count = count+1
	#the reverse of the result list has products of the 'after' category
	result = result[::-1]
	
	#now do the before category:
	before = 1
	for i in range(1,len(nums)):
		result[i] = result[i] * before * nums[i-1]
		before = before * nums[i-1] 
	print(result)
	return

array_product([1,2,3,4,5])