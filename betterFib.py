def fill_result(fib_res, ri):
	if ri == 2:
		fib_res[ri] = fib_res[0] + fib_res[1]
	elif ri == 1:
		fib_res[ri] = fib_res[0] + fib_res[2]
	else:
		fib_res[ri] = fib_res[1] + fib_res[2]
	return

def fib(n):
	fib_res = [0,1,0]
	result_index = 2

	for i in xrange(n-1):
		fill_result(fib_res, result_index)
		result_index = (result_index + 1) % 3
	print fib_res[result_index-1]

fib(9)