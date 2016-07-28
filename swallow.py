def rec_swallow(s, index, n):
	'''
	recursive swallow: prints out if it can swallow and calls itself recursively
	till not more can be swallowed
	'''
	#can i swallow?
	if (index + (n-1)) < (len(s)-1):
		after = index + n
		print(s[:index] + str(n) + s[after:])
		rec_swallow(s, index+1, n)
	else:
		return


def swallow(s, n):
	index = 1
	while (index + (n-1)) < (len(s) -1):
		after = index + n
		print(s[:index] + str(n) + s[after:])
		index = index + 1
	return
	


def numeronyms(s):
	size = len(s) - 2
	while size >= 2:
		swallow(s, size)
		size = size - 1


numeronyms("nailed")
