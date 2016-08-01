'''given T = dogthecatcatthedog and A = ["the", "cat"] (n words of k length) output 3, 9 since the concatenation thecat and catthe is found in T at those indices. all n words should be part of the concatenation pattern, each word is size k and order does not matter
'''

def resetDict(d):
	for key in d:
		d[key] = 1
	return d


def checkDict(d):
	for key in d:
		if d[key] != 2:
			return False
	return True


def searchConcat(s, words):
	rl = list()
	i = 0
	k = len(words[0])
	d = dict()

	tmp = "$" * k
	original_l = len(s)
	s = s + tmp

	for w in words:
		d[w] = 1

	while i < original_l:
		ss = s[i:i+k]
		if ss in d:
			answer = i
			d[ss] = 2
			count = 1
			i = i + k
			while count != len(words) and i < original_l:
				ss = s[i:i+k]
				if ss in d:
					d[ss] = 2
					count = count + 1
					i = i + k
			if count == len(words):
				if checkDict(d):
					rl.append(answer)
			resetDict(d)
		else:
			i = i + k
	return rl

print(searchConcat("dogthecatcatthedog", ["the", "cat"]))