def palinSize(strText):
	if len(strText) == 1:
		return 1
	if len(strText) == 2:
		if strText[0] == strText[-1]:
			return 2
		else:
			return -1

	if strText[0] == strText[-1]:
		size =  1 + palinSize(strText[1:-1])
		return size

def  LongestPalindromicSubstring(strText):




LongestPalindromicSubstring("madam")


madam
aamadam