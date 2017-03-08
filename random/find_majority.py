'''
Find the majority element in a list/array if the majority element appears atleast more than half the number of times
'''
def find_maj(arr):
    print(len(arr))
    cand = arr[0]
    cand_score = 1
    for i in range(1, len(arr)):

        if cand_score == 0:
            cand = arr[i]
            cand_score = 1

        if arr[i] == cand:
            cand_score = cand_score + 1

        if arr[i] != cand:
            cand_score = cand_score - 1

    count = 0
    for i in range(len(arr)):
        if arr[i] == cand:
            count = count + 1

    if count >= len(arr)/2:
        print("Candidate found: " + str(cand))


find_maj([1,1,2,2,2,3,1,1,2,3,3,3,2,2,3,3,3,3,3])