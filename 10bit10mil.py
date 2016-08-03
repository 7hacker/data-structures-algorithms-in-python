'''
Given 10 million 10 bit ints, sort these efficiently
'''
import random

def genRandom10bitVal():
	return random.randint(0,1023)

def genInts(howmany):
	ret = []
	for i in range(howmany):
		ret.append(str(genRandom10bitVal()))
	return ret

def sortNums(numlist):
	d = {}
	sList = []
	for i in range(1024):
		d[i] = 0
	for n in numlist:
		d[int(n)] = d[int(n)] + 1
	for key in d:
		for j in range(d[key]):
			sList.append(str(key))
	return sList

unsortedFname = "unsorted.txt"
sortedFname = "sorted.txt"

numList = genInts(10000)
fop = open(unsortedFname, 'w')
fop.write(" ".join(numList))
fop.close()

sortedNums = sortNums(numList)
fop = open(sortedFname, 'w')
fop.write(" ".join(sortedNums))
fop.close()
