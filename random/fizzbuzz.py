'''
Write a function that iterates through a range of numbers from 1 to 50 and prints "Fizz" if the number is a multiple of 3, prints "Buzz" if the number is multiple of 5, and print "FizzBuzz" if the number is a multiple of both 3 and 5.  
'''

def fizzbuzz(n):
	for i in xrange(1,n):
		s = str(i) + ":"
		if i%3 == 0:
			s = s + "Fizz"
		if i %5 == 0:
			s = s + "Buzz"
		print s
	return

fizzbuzz(50)