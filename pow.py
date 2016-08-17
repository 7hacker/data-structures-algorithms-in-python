'''
Implement the pow function efficiently
'''
def foo_pow(d, p):
    if p == 1:
        return d
    if p == 0:
        return 1

    t = foo_pow(d, p/2)
    
    if p % 2 == 0:
        return t * t
    else:
        if (p > 0):
            return d * t * t
        else:
            return (t * t)/d

print(foo_pow(5,5))