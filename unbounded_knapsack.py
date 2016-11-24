def _unbounded(a, i, k, cache):
    if i >= len(a):
        if not cache[i][k]:
            cache[i][k] = k
        return cache[i][k]
    else:
        c = 0
        diffs = []
        while c * a[i] <= k:
            if not cache[i][k]:
                cache[i][k] = _unbounded(a, i+1, k-(c*a[i]), cache)
            diffs.append(cache[i][k])
            c = c + 1
        return min(diffs)
    

def unbounded(a, k):
    cache = [[None]*(k+1) for i in xrange(len(a)+1)]
    #print(cache)
    c = 0
    diffs = []
    while c * a[0] <= k:
        cache[0][k-(c*a[0])] = _unbounded(a,1,k-(c*a[0]), cache)
        diffs.append(cache[0][k-(c*a[0])])            
        c = c + 1
    #print(cache)
    return k- min(diffs)
    

print(unbounded([1,6,9],12))