'''
Edit distance using Dynamic programming
'''
from rcviz import callgraph, viz

@viz
def edit_distance_dynamic_rec(source, target, i, j):
	
	if i == len(source) and j == len(target):
		if cache[i][j] is not None:
			print("Cache lookup for " + str(i) + "," + str(j))
			return cache[i][j]
		s = ""
		t = ""
		edit_distance_dynamic_rec.track(source_now=s)
		edit_distance_dynamic_rec.track(target_now=t)
		cache[i][j] = 0
		return cache[i][j]

	if i == len(source):
		if cache[i][j] is not None:
			print("Cache lookup for " + str(i) + "," + str(j))
			return cache[i][j]
		s = ""
		t = target[j:]
		edit_distance_dynamic_rec.track(source_now=s)
		edit_distance_dynamic_rec.track(target_now=t)
		#target has additional chars to add into source
		cache[i][j] = len(target) - j
		return cache[i][j]

	if j == len(target):
		if cache[i][j] is not None:
			print("Cache lookup for " + str(i) + "," + str(j))
			return cache[i][j]
		t = ""
		s = source[i:]
		edit_distance_dynamic_rec.track(source_now=s)
		edit_distance_dynamic_rec.track(target_now=t)
		#source has additional chars to delete
		cache[i][j] = len(source) - i
		return cache[i][j]

	else:
		if cache[i][j] is not None:
			print("Cache lookup for " + str(i) + "," + str(j))
			return cache[i][j]
		s = source[i:]
		t = target[j:]
		edit_distance_dynamic_rec.track(source_now=s)
		edit_distance_dynamic_rec.track(target_now=t)
		if source[i] == target[j]:
			cache[i][j] = edit_distance_dynamic_rec(source, target, i+1, j+1)
			return cache[i][j]

		else:
			cache[i][j] = 1 + min (edit_distance_dynamic_rec(source, target, i+1, j+1),
							edit_distance_dynamic_rec(source, target, i, j+1),
							edit_distance_dynamic_rec(source, target, i+1, j))
			return cache[i][j]


source = "kitten"
target = "sitting"
x = len(source) + 1
y = len(target) + 1
cache = [[None]*y for i in range(x)]

print(edit_distance_dynamic_rec(source, target, 0, 0))
print(cache)
callgraph.render("edit_distance_dynamic_rec_kittenTOsitting.png")
