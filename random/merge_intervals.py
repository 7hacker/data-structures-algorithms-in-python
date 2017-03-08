'''
Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity.
For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }. The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}. Similarly {5, 7} and {6, 8} should be merged and become {5, 8}
'''

def merge_intervals(intervals):
	if not len(intervals):
		return []
	merged = [intervals[0]]
	for i in xrange(1,len(intervals)):
		if intervals[i][0] > merged[-1][1]:
			merged.append(intervals[i])
		else:
			p = merged.pop(-1)
			merged.append((p[0], max(p[1], intervals[i][1])))
	return merged

print merge_intervals([(1,3), (2,4), (5,7), (6,8)])
print merge_intervals([(1,9), (2,4), (4,7), (6,8)])