SEP = "#"
ESCAPE= '.'

def mynewencode(l):
	estr = ""
	for item in l:
		newitem = ""
		for c in item:
			if c == SEP or c == ESCAPE:
				newitem = newitem + ESCAPE + c
			else:
				newitem = newitem + c
		estr = estr + SEP + newitem
	return estr


def myencode(l):
	estr = ""
	if len(l):
		estr = estr + str(len(l)) + SEP
		for item in l:
			estr = estr + str(len(item)) + SEP + str(item)
	return estr

def mydecode(estr):
	if not len(estr):
		return []
	myl = estr.split(SEP,1)
	size = int(myl[0])
	remainder = myl[1]
	rl = []
	for i in xrange(size):
		myl = remainder.split(SEP, 1)
		count = int(myl[0])
		remainder = myl[1]
		item = remainder[:count]
		remainder = remainder[count:]
		rl.append(item)
	return rl

def testfoo(original, encoded):
	if mydecode(encoded) == original:
		return True
	else:
		return False

l = ['aa#a.', '#bbb', 'cde']
print mynewencode(l)
l = ['#', '#', '#']
print mynewencode(l)

'''
l = ['aaa', 'bbb', 'cde']
print testfoo(l, myencode(l)) #True
l = []
print testfoo(l, myencode(l)) #True
l = ['123456789123']
print testfoo(l, myencode(l)) #True
l = ['', '', '']
print testfoo(l, myencode(l)) #True
l = ['###', '###', '###']
print testfoo(l, myencode(l)) #True

l = ['###', '3333', '$%&!!!!***']
print testfoo(l, myencode(l)) #True
'''



