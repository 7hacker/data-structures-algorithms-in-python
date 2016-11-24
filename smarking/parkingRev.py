def sanitize(s):
	s = s.replace(" ", "")
	s = s.rstrip()
	if s[0] == "(":
		return float(s[1:-1])
	else:
		return float(s)

def getMin(l):
	mn = l[0]
	mni = 0
	for i in xrange(1,len(l)):
		if l[i] < mn:
			mn = l[i]
			mni = i			
	return (mn, mni)

def updateItem(item, l, i):
	l[i] = item
	return l


top5Trans = [0] * 5
fo = open("events_time.csv", "r")
lines = fo.readlines()
for line in lines:
	sl = line.split(",")
	if "transient" in sl[1]:
		v = sanitize(sl[2])
		mn, i = getMin(top5Trans)
		if v > mn:
			#print top5Trans
			top5Trans = updateItem(v, top5Trans, i)
			#print top5Trans
print top5Trans			

		


