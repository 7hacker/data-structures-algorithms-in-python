'''
Quicksort!
'''

def swap(a, i, j):
    if i != j:
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return

def partition_2(a, low, high):
    #from Programming Pearls
    pivot = a[low]
    m = low
    for i in range(low+1, high+1):
        if a[i] < pivot:
            m = m + 1
            swap(a, m, i)
    swap(a, low, m)
    return m

def quicksort(a, low, high):
    if low < high:
        p= partition_2(a, low, high)
        quicksort(a, low, p-1)
        quicksort(a, p+1, high)
    return a

a = [89, 24, 34, 12, 2, 43, 523, 52, 642, 21, 35, 6, 124, 99, 44, 325, 21, 646, 363, 634 , 72, 31, 6146, 46, 134, 647, 616]
#a = [4, 2, 5, 6]
quicksort(a, 0, len(a)-1)
print(a)

