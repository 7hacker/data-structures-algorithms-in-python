'''
a  merge sort with a recursive merge
'''
from rcviz import callgraph, viz


def rec_merge(a, b, ai, bi, m, mi):
	if ai >= len(a):
		for x in range(bi, len(b)):
			m.append(b[x])
		return
	if bi >= len(b):
		for x in range(ai, len(a)):
			m.append(a[x])
		return
	if a[ai] <= b[bi]:
		m[mi] = a[ai]
		rec_merge(a, b, ai+1, bi, m, mi+1)
	else:
		m[mi] = b[bi]
		rec_merge(a, b, ai, bi+1, m, mi+1)

def mergesort(a, low, high):
	if low < high:
		m1 = mergesort(a, low, (low+high/2))
		m2 = mergesort(a, (low+high)/2 + 1, high)
		mlen = 0
		if m1:
			mlen = mlen + len(m1)
		if m2:
			mlen = mlen + len(m2)
		if mlen > 0:
			mlen = mlen -1
		merged = [None] * mlen
		rec_merge(m1, m2, 0, 0, merged, 0)
		return merged


#a = [1, 7, 11]
#b = [2, 6, 12]
#mlen = len(a) + len(b) -1
#merged = [None] * mlen
#print(merged)
#rec_merge(a, b, 0, 0, merged, 0)
#print(merged)

us = [23, 2, 153, 3256, 35, 643, 23, 653, 3423, 756,32]
print(mergesort(us, 0, len(us)-1))