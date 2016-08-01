'''
Print out the pascal triangle for value: n
'''
def pascal(n):
	result = []
	p_one = [1]
	p_two = [1, 1]
	result.append(p_one)
	result.append(p_two)

	for k in range(2,n):
		p = list()
		prev = result[k-1]
		p.append(1)
		i = 0
		while i < len(prev) - 1:
			ele = prev[i] + prev[i+1]
			p.append(ele)
			i = i + 1
		p.append(1)
		result.append(p)
	for r in result:
		print(r)
		
pascal(6)