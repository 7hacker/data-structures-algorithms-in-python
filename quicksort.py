'''
Quicksort!
'''

def swap(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t
	return


def partition(a, low, high):
	pivot = a[low]
	start = low+1
	end = high
	done = False
	while not done:
		while start <= end and a[start] <= pivot:
			start = start + 1
		while a[start] >= pivot and end >= start:
			end = end - 1
		if start > end:
			done = True
		else:
			swap(a, start, end)
	swap(a, low, end)
	return end



def quicksort(a, low, high):
	if low < high:
		p= partition(a, low, high)
		quicksort(a, low, p-1)
		quicksort(a, p+1, high)
	return a

#a = [89, 24, 34, 12, 2, 43, 523, 52, 642, 21, 35, 6, 124, 99]
a = [3, 1, 0, 4, 7]
quicksort(a, 0, len(a)-1)
print(a)