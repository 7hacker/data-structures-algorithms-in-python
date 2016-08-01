'''
cut a rope of size n such that the product of the cuts is maximized atleast one cut must be made example: rope of size = 4 the best cut is 2,2 (2 * 2 = 4) as opposed to 3,1 (3* 1 = 3) or 1,3 or 1,2,1, 2,1,1, 1,1,1,1
'''

def rec_rope_cut(cutAt, remainder_rope, product, size):
	return rec_rope_cut()

def rope_cut(size):
	return rec_rope_cut(0, size-1, 1, size)

print(rope_cut(4))