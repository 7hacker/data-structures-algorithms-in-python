'''
Generate some Primes using a bit array - a cool technique I learnt
'''
from bitarray import bitarray

class Primes:
	def __init__(self, howmany):
		self.n = howmany
		self.primeBitArray = bitarray(howmany)
		self.primeList = []
		#Everyone is a prime number!
		self.primeBitArray.setall(True)
		#make some prime numbers that you know
		self.primeBitArray[0] = 0
		self.primeBitArray[1] = 0
		self.primeBitArray[2] = 1
		self.primeBitArray[3] = 1
		self.primeBitArray[5] = 1
		self.primeBitArray[7] = 1
		#for each number in the bit array, their multiples can be set to False
		for i in range(2,howmany):
			for j in range(i*2, howmany, i):
				self.primeBitArray[j] = 0
		#magic! now you have all prime numbers in the bit array
		
	def getPrimeList(self):
		ret = []
		for i in range(self.n):
			if self.primeBitArray[i]:
				ret.append(i)
		return ret


