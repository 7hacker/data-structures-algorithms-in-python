#http://stackoverflow.com/questions/727707/finding-all-combinations-of-well-formed-brackets

d = dict()

def bracketsN(n, s,d, key):
    if n == 1:
        mid = "(" + s + ")"
        behind = "()" + s
        after = s + "()"
        if mid not in d[key]:
            d[key].append(mid)

        if behind not in d[key]:
            d[key].append(behind)

        if after not in d[key]:
            d[key].append(after)
        return
    else:
        mid = "(" + s + ")"
        bracketsN(n-1, mid,d, key)
        behind = "()" + s
        bracketsN(n-1, behind,d, key)
        after = s + "()"
        bracketsN(n-1, after,d, key)
                
def  WellFormedBrackets():
    d = dict()
    #bracketsN(3, "", d)
    #print(d.keys())
    
    for i in range(1,11):
        d[i] = list()
        bracketsN(i, "", d, i)

    for i in range(1,11):
        print(d[i])
    
    return


WellFormedBrackets()