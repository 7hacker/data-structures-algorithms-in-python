from rcviz import callgraph, viz

def find_segment_tree_size(n):
	#segment trees are 2n if n is a power of 2
	#if n is not a power of 2, find k > n that is the closest power of 2 from n and return 2k
	size = 1
	while (size < n):
		size = size << 1
	return size << 1
@viz
def buildSegTree(t, n, start, end, ti):
	#builds a sum segment tree
	if start > end:
		return
	if start == end:
		t[ti] = n[start]
		return t[ti]
	else:
		left = buildSegTree(t, n, start, (start+end)/2, (ti * 2) + 1)
		right = buildSegTree(t, n, (start+end)/2 + 1, end, (ti * 2) + 2)
		t[ti] = left + right
		return t[ti]


def buildMinSegTree(t, n, start, end, ti):
	#builds a min segment tree
	if start > end:
		return
	if start == end:
		t[ti] = n [start]
		return t[ti]
	else:
		left = buildMinSegTree(t, n, start, (start+end)/2, (ti * 2) + 1)
		right = buildMinSegTree(t, n, (start+end)/2+1, end, (ti * 2) + 2)
		t[ti] = min(left, right)
		return t[ti]

def querySegTree(t, i, j):
	#query the result of range i-j where i <= j
	if i > j:
		return None
	else:
		


nums = [1,3,5,7, 9, 11]
segTreeSize = find_segment_tree_size(len(nums))
segTree = [None] * segTreeSize
buildMinSegTree(segTree, nums, 0, len(nums)-1, 0)
print(segTree)
callgraph.render("segmenttree.png")


