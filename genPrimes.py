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
		# 0 and 1 are not prime numbers
		self.primeBitArray[0] = 0
		self.primeBitArray[1] = 0
		#for each number in the bit array, their multiples can be set to False
		for i in range(2,howmany):
			for j in range(i*2, howmany, i):
				self.primeBitArray[j] = 0
		#magic! now you have all prime numbers in the bit array
		for i in range(self.n):
			if self.primeBitArray[i]:
				self.primeList.append(i)
		
	def getPrimeList(self):
		return self.primeList

