from rcviz import callgraph, viz

#longest increasing subsequence
@viz
def rec_lis(A, i):
	if i == len(A) -1:
		return (1, A[i])
	else:
		(lth, val) = rec_lis(A, i + 1)
		if val > A[i]:
			return (lth+1, A[i])
		else:
			return (lth, A[i])


#(lth, _) = rec_lis([-7, 10, 9, 2, 3, 8, 8, 1], 0)
#print(lth)
(lth, _) = rec_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 0)
print(lth)
'''
(lth, _) = rec_lis([1, 5, 2, 3], 0)
print(lth)
(lth, _) = rec_lis([9, 8, 7, 6, 5, 4, 3], 0)
print(lth)
(lth, _) = rec_lis([1,5,7,8,9], 0)
print(lth)
(lth, _) = rec_lis([20,79,51,33,108,200], 0)
print(lth)
'''

callgraph.render("lis.png")
