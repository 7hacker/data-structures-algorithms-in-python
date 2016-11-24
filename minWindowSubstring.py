def reset_set(t):
	d = dict()
	for c in t:
		if c in d:
			d[c] = d[c] + 1
		else:
			d[c] = 1
	return d

def found_all(target_d):
	for k in target_d:
		if target_d[k] == -1:
			return (False, True)
	for k in target_d:
		if target_d[k] > 0:
			return (False, False)
	print "Found all!"
	return (True, True)

def can_shrink(target_d, c):
	if c in target_d:
		return False
	else:
		return True

import sys
def minWindowSubstring(s, t):
	target_d = reset_set(t)
	start = 0
	end = 1
	window_size = sys.maxint

	if s[start] in target_d:
		target_d[s[start]] = target_d[s[start]] - 1

	while end < len(s):
		if s[end] not in target_d:
			end = end + 1
		else:
			target_d[s[end]]  = target_d[s[end]] - 1
			(found, reset) = found_all(target_d)
			if found:
				while can_shrink(target_d, s[start]):
					start = start + 1

				window_size = min(window_size, end-start+1)
				target_d = reset_set(t)
				start = end
				target_d[s[start]] = target_d[s[start]] - 1
				end = end + 1
			else:
				if reset:
					target_d = reset_set(t)
					start = end
					target_d[s[start]] = target_d[s[start]] - 1
					end = end + 1
				else:
					end = end + 1

			

	return window_size

print minWindowSubstring("dxbanc", "abc")