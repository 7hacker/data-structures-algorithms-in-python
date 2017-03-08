'''
you and your friend are playing a game with coins, such that each coin has a value, and you can pick a coin from the start of a list or end of a list. If you begin first, and your friend is equally competent as you, what is the best choice you can make?
'''
from rcviz import callgraph, viz


@viz
def coin_play(coins, start, end, cache):
    if start > end:
        return 0
    if start == end:
        if not cache[start][start]:
            cache[start][start] = coins[start]
        return cache[start][start]
    else:
        if not cache[start+2][end]:
            cache[start+2][end] = coin_play(coins, start+2, end, cache)
        choice1_a = cache[start+2][end]

        if not cache[start+1][end-1]:
            cache[start+1][end-1] = coin_play(coins, start+1, end-1, cache)
        choice1_b = cache[start+1][end-1]

        if not cache[start][end-2]:
            cache[start][end-2] = coin_play(coins, start, end-2, cache)
        choice2_a = cache[start][end-2]

        choice2_b = cache[start+1][end-1]

        choice1 = coins[start] + min(choice1_a, choice1_b)
        choice2 = coins[end] + min(choice2_a, choice2_b)
        return max(choice1, choice2)


def coin_play_iterative(cache, coins):
    for i in range(len(coins)):
        cache[i][i] = coins[i]
    for i in range(len(coins)):
        for j in range(i, len(coins)):
            if i != j:
                x = cache[i+2][j] 
                y = cache[i+1][j-1]
                z = cache[i][j-2]
                cache[i][j] = max(
                    (coins[i] + min(x, y)),
                    (coins[j] + min(y, z))
                    )
    print(cache)
    return cache[0][len(coins)-1]




coins = [8, 15, 3, 7]
size = len(coins) + 2
cache = [[0]*size for i in range(size)]
#print(coin_play(coins, 0, len(coins)-1, cache))
print(coin_play_iterative(cache, coins))
callgraph.render("coin_play.png")
