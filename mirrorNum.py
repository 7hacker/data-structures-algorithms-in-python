def getMirrror(n):
    sn = str(n)
    isEven = len(sn) % 2 == 0
    if isEven:
        left = sn[:len(sn)/2]
        right = left[::-1]
        return int(left + right)
    else:
        mid = sn[len(sn)/2]
        left = sn[:len(sn)/2]
        right = left[::-1]
        return int(left + mid+ right)





def roundUp(n):
    l = len(str(n))
    return int(((n/pow(10, l-1)) + 1) * pow(10,l-1))

print(getMirrror(12345))
print(getMirrror(12345678))
print(roundUp(1891))