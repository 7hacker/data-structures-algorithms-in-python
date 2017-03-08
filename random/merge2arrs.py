'''
Given 2 arrs: Short and Long of same size (n), that are already sorted return the sorted long array in linear time, merging the two arrays
'''




def merge2(arr1, arr2):
    #arr1 = len(arr2)/2
    i = 0
    j = 0
    while i < len(arr1):
        if arr1[i] > arr2[j]:
            i = i + 1
        else:
            t = arr2[j]
            arr2[j] = arr1[i]
            arr1[i] = t
        i = i + 1
        j = j + 1

    print(arr1)
    print(arr2)



merge2([4,5], [4,5,0,0])