def countbits(n):
	count = 0
	while(n):
		count = count + (n & 1)
		n = n >> 1
	return count

d = {}
for i in range(429496729):
	d[i] = 0

print(len(d.keys()))
#print(countbits(9))