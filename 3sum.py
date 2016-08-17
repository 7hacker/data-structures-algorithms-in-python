'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''
from rcviz import callgraph, viz

def sum3_iterative(a):
    res = []
    a.sort()
    for i in range(0, len(a)-2):
        if (i == 0 or a[i] > a[i-1]):
            j = i + 1
            k = len(a)-1
            while j < k :
                if a[i] + a[j] + a[k] == 0:
                    res.append([a[i], a[j], a[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and a[j] == a[j-1]:
                        j = j + 1
                    while j < k and a[k] == a[k+1]:
                        k = k - 1
                elif a[i] + a[j] + a[k] < 0:
                    j = j + 1
                else:
                    k = k -1
    print(res)

@viz
def sum3_rec(a, i, chosen):
    if i >= len(a):
        if len(chosen) == 3:
            if chosen[0] + chosen[1] + chosen[2] == 0:
                print(chosen)
        return
    else:
        if len(chosen) == 3:
            if chosen[0] + chosen[1] + chosen[2] == 0:
                print(chosen)
            return
        elif len(chosen) > 3:
            return
        else:
            sum3_rec(a, i+1, chosen)
            nl = list(chosen)
            nl.append(a[i])
            sum3_rec(a, i+1, nl)

a = [-1, 0, 1, 2, -1]
sum3_iterative(a)
#callgraph.render("3sum_rec.png")
