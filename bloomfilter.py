'''
a bloom filter of /usr/share/dict/words
'''
from bitarray import bitarray
import mmh3
import random

class BloomFilter:
	def __init__(self, size=pow(2,10), k=3):
		self.db = bitarray(size)
		self.k = k
		self.size = size
		return

	def getHashes(self, item):
		bits = []
		for i in range(self.k):
			bits.append(mmh3.hash(item, i) % self.size)
		#print("For item: " + item + " bits are : " + str(bits))
		return bits

	def add(self, item):
		bits = self.getHashes(item.lower())
		for b in bits:
			self.db[b] = 1
		return

	def test(self, item):
		bits = self.getHashes(item.lower())
		#print("Test for Item: " +  item + ":"+ str(bits))
		for b in bits:
			if not self.db[b]:
				return False
		return True

	def showBloom(self):
		print(self.db)
		return


def loadBloomFilter(bf, f):
	fl = open(f)
	lines = fl.readlines()
	for l in lines:
		bf.add(l.rstrip())


if __name__ == '__main__':
	bf = BloomFilter(15485863, 3)
	loadBloomFilter(bf, "/usr/share/dict/words")
	print("Apple: " + str(bf.test("apple")))
	print("Orange: " + str(bf.test("OrANGe")))
	print("Grape: " + str(bf.test("GRaPE")))
	print("Annoying: " + str(bf.test("Annoying")))
	print("Fantastic: " + str(bf.test("FANTASTIC")))
	print("Green: " + str(bf.test("green")))
	print("Nirmal: " + str(bf.test("nirmal")))
	print("Adriana: " + str(bf.test("adriana")))
	print("InterviewKickstart: " + str(bf.test("interviewkickstart")))
	print("Bazzzinnnggaaa!!: " + str(bf.test("Bazzzinnnggaaa")))
	#bf.showBloom()




