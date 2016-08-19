'''
find the longest repeated(char) substring in an input string. Eg: input = aabbbc;output = bbb , input = abc; output = a(or b or c), input=foofoofoo;output=oo
'''

def longestRepeatedChar(in_str):
    if not in_str:
        return None
    candidate = in_str[0]
    candidate_count = 1
    i = 1
    while i < len(in_str):
        if in_str[i] != candidate:
            possible_candidate = in_str[i]
            possible_candidate_count = 1
            j = i + 1
            while j < len(in_str):
                if in_str[j] == possible_candidate:
                    possible_candidate_count = possible_candidate_count + 1
                    j = j + 1
                else:
                    break
            if possible_candidate_count > candidate_count:
                candidate_count = possible_candidate_count
                candidate = in_str[j-1]
            i = j
        else:
            candidate_count = candidate_count + 1
            i = i + 1
            
    return candidate * candidate_count



print(longestRepeatedChar("aaaabcddeeefg"))


