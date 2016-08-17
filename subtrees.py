'''
what are the structurally unique binary trees that can be formed for size n?
'''
from rcviz import callgraph, viz

num_trees_result = {}
num_trees_result[0] = 1
num_trees_result[1] = 1


@viz
def num_trees(n):
    if n == 1 or n == 0:
        return num_trees_result[n]

    total = 0

    for k in range(1, n+1):
        if k-1 not in num_trees_result:
            left = num_trees(k-1)
            num_trees_result[k-1] = left
        else:
            left = num_trees_result[k-1]

        if n-k not in num_trees_result:
            right = num_trees(n-k)
            num_trees_result[n-k] = right
        else:
            right = num_trees_result[n-k]

        total = total + (left * right)

    return total

print(num_trees(4))
callgraph.render("possible_trees_dyn.png")