'''
what is the size of Longest substring with at most 2 distinct characters eg: s = "eceba" output : 3 ("ece")
'''


def buildWindow(i, s):
    if i > len(s)-1:
        return None
    else:
        size = 1
        first = s[i]
        second = s[i]
        while i < len(s) - 1:
            i = i + 1
            second = s[i]
            size = size + 1
            if second != first:
                break
        if first == second:
            return None
        else:
            return (first, second, size, i)

def growWindow(s, first, second, size, i):
    if i > len(s)-1:
        return (first, second, size, i)
    else:
        newSize = size
        k = i
        while k < len(s) -1:
            k = k + 1
            if s[k] == first or s[k] == second:
                newSize = newSize + 1
            else:
                break
        if newSize > size:
            return(first, second, newSize, k)
        else:
            return(first, second, size, i)


def longestSub(s):
    if len(s) < 2:
        return None
    i = 0
    maxsize = 0
    while i <= len(s):
        p = buildWindow(i,s)
        print(p)
        if p is not None:
            t = growWindow(s, p[0], p[1], p[2], p[3])
            print(t)
            if t[2] > maxsize:
                maxsize = t[2]
            i = i + 1
        else:
            i = i + 1

    print(maxsize)

longestSub("ecebaaaddddd")