from rcviz import callgraph, viz

@viz
def cc(coins, amt):
	if amt == 0:
		return 1
	else:
		for c in coins:
			if c == 1:
				print("Choosing 1")
			if amt - c >= 0:
				res = 1 + cc(coins, amt - c)
				return res



coins = [25, 5, 1, 10]
amt = 76
change = 1000 #some max

for c in coins:
	if c == 1:
		print("Choosing 1")
	res = cc(coins, amt - c)
	if res < change:
		change = res

print(change)
callgraph.render("cc.png")

