'''
count the bits set in a value n
'''
def countbits(n):
	count = 0
	while(n):
		count = count + (n & 1)
		n = n >> 1
	return count

print(countbits(9))