'''
Quick select Median finding
'''
def swap(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t


def partition(a, low, high):
	pivot = a[low]
	m = low
	for i in xrange(low+1, high+1):
		if a[i] < pivot:
			m = m + 1
			swap(a, m, i)
	swap(a, low, m)
	return m




def find_median(a):
	low = 0
	high = len(a)-1
	found = False
	while not found:
		p = partition(a, low, high)
		if p == median_index:
			found=True
		elif p < median_index:
			low = p + 1
		else:
			high = p - 1

	return a[median_index]

print(find_median([7, 20, 4, 1, 5, 11, 16,9, 8]))