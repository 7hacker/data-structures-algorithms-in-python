def wordExists(w):
	return  w in ["i", "a", "am", "happy", "after", "noon", "afternoon", "wow", "mhap", "py"]

def splitString(s, i, res_list, master_list):
	if i >= len(s):
		list_copy = list(res_list)
		master_list.append(list_copy)
		return
	else:
		size = 1
		while i + size <= len(s):
			if wordExists(s[i:i+size]):				
				res_list.append(s[i:i+size])
				'''
				if i+size >= len(s):

					master_list.append(res_list)
					print "Ended"
					print res_list
					return
				'''
				splitString(s, i+size, res_list, master_list)
				res_list.pop()
				size  = size + 1
			else:
				size = size + 1


s = "afternoon"
res_list = list()
master_list = list()
splitString(s, 0, res_list, master_list)
print "Outside"
print master_list
