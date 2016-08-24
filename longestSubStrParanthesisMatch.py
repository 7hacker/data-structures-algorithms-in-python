'''
find the longest substring with matching paranthesis. example: () is 2, ((()), is 4, ()(()) is 6, ((((( is 0, ()) is 2, ((((())(((() is 4
'''

from stack import Stack

def p_match(ex):
    s = Stack()
    maxcount = 0
    count = 0
    for c in ex:
        if c == "(":
            if s.size() > 0:
                if count > maxcount:
                    maxcount = count
                count = 0
            s.push(c)
        else:
            #assume its )
            if s.size() and s.peek() == "(":
                s.pop()
                count = count + 2
                #print(count)
    if count > maxcount:
        maxcount = count
    return maxcount

print(p_match("((((())(((()"))