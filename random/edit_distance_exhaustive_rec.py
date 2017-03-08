'''
Edit distance using Exhaustive Search
'''
from rcviz import callgraph, viz

#@viz
def cost(source, target, i, j):
    if source[i] == target[j]:
        return 0
    else:
        return 1

#@viz
def edit_distance_exhaustive(source, target, i, j):
    if i == len(source) and j == len(target):
        s = ""
        t = ""
        #edit_distance_exhaustive.track(source_now=s)
        #edit_distance_exhaustive.track(target_now=t)
        return 0
    if i == len(source):
        s = ""
        t = target[j:]
        #edit_distance_exhaustive.track(source_now=s)
        #edit_distance_exhaustive.track(target_now=t)
        #target has additional chars to add into source
        return len(target) - j
    if j == len(target):
        t = ""
        s = source[i:]
        #edit_distance_exhaustive.track(source_now=s)
        #edit_distance_exhaustive.track(target_now=t)
        #source has additional chars to delete
        return len(source) - i
    else:
        s = source[i:]
        t = target[j:]
        #edit_distance_exhaustive.track(source_now=s)
        #edit_distance_exhaustive.track(target_now=t)
        if source[i] == target[j]:
            return edit_distance_exhaustive(source, target, i+1, j+1)
        else:
            return min (edit_distance_exhaustive(source, target, i+1, j+1) + 1,
                        edit_distance_exhaustive(source, target, i, j+1) + 1,
                        edit_distance_exhaustive(source, target, i+1, j) + 1)


print(edit_distance_exhaustive("kitten", "sitting", 0, 0))
#callgraph.render("edit_distance_exhaustive_catTOhat.png")
