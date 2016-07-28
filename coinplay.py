from rcviz import callgraph, viz

@viz
def coin_play(coins, start, end, player1, player2):
	if start == end:
		return coins[start]
	elif len(coins) == 2:
		if player1:
			return max(coins[start], coins[end])
		else:
			return min(coins[start], coins[end])
	elif player1:
		choice1 = coins[start] + coin_play(coins, start+1, end, False, True)
		choice2 = coins[end] + coin_play(coins, start, end-1, False, True)
		return max(choice1, choice2)
	else:
		choice1 = coin_play(coins, start+1, end, True, False)
		choice2 = coin_play(coins, start, end-1, True, False)
		return min(choice1, choice2)

coins = [8,15,3,7]
print(coin_play(coins, 0, len(coins)-1, True, False))
callgraph.render("coin_play.png")
