def ways_to_make_change(coins, target, ways):
	if target < 0:
		return
	if target == 0:
		print(ways)
		return
	for c in coins:
		s = ways
		ways_to_make_change(coins, target-c, s + "," + str(c))


coins = [1,2,3]
ways_to_make_change(coins, 4, "")