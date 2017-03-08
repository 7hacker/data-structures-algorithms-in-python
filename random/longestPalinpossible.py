'''
http://www.geeksforgeeks.org/find-longest-palindrome-formed-by-removing-or-shuffling-chars-from-string/
'''

def find_longest_palin(s):
	d = {}
	for char in s:
		if char not in d.keys():
			d[char] = 1
		else:
			d[char] = d[char] + 1

	start = ""
	end = ""
	mid = ""

	for char in d:
		while d[char] >= 2:
			d[char] = d[char] - 2
			start = start + char
			end = char + end
	for char in d:
		if d[char] == 1:
			mid = char

	return start + mid + end

print find_longest_palin("abbaccd")
print find_longest_palin("aabbcc")
print find_longest_palin("abc")
print find_longest_palin("aba")