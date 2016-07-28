def  printSnakeString():
	s = "Google Worked"
	result = []

	for i in range(3):
	    ri = []
	    for i in range(len(s)):
	        ri.append(" ")
	    result.append(ri)

	#bottom line
	for i in range(0,len(s),4):
		if s[i] == " ":
			result[0][i] = "~"
		else:
			result[0][i] = s[i]

	#middle line
	for i in range(1,len(s),2):
		if s[i] == " ":
			result[1][i] = "~"
		else:
			result[1][i] = s[i]
	#last line
	for i in range(2,len(s),4):
		if s[i] == " ":
			result[2][i] = "~"
		else:
			result[2][i] = s[i]
   	
	print("".join(result[2]))
	print("".join(result[1]))
	print("".join(result[0]))

	return

printSnakeString()
