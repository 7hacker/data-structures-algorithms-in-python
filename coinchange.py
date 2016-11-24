'''
Given N coins make change, C with the minimum number of coins. Output the coins used to make the Change. If there are more than one such sets, output them all. The same coin can be used repeatedly
'''
import sys
from rcviz import callgraph, viz



@viz
def coinchange(coins, amt, cache):
    if amt < 0:
        return sys.maxint
    if amt == 0:
        return cache[0]
    choices = []
    for c in coins:
        if not cache[amt-c]:
            cache[amt-c] = coinchange(coins, amt-c, cache)
        choices.append(cache[amt-c])
    cache[amt] = 1 + min(choices)
    return cache[amt]


def coinchange_iterative(coins, amt, cache):
    cache[0] = 0 # 0 coins req to make change of 0
    for c in coins:
        cache[c] = 1 # 1 coin req to make change of amt = value of coin
    for i in range(len(cache)):
        if cache[i] is None:
            choices = []
            for c in coins:
                if i-c >= 0:
                    choices.append(cache[i-c])
            if len(choices):
                cache[i] = 1 + min(choices)
            else:
                cache[i] = sys.maxint
    return cache[-1]


def print_coins(coins, amt, cache):
    res = []
    min_list = []
    while amt != 0:
        for c in coins:
            if amt >= c:
                if cache[amt-c] == cache[amt] -1:
                    min_list.append(amt-c)
                    amt = amt -c
                    #print(min_list)

    print(min_list)


coins = [1,2,3]
amt = 4
cachesize = amt+1
cache = [None] * cachesize
cache[0] = 0
print(cache)
#print(coinchange(coins, amt, cache))
print(coinchange_iterative(coins, amt, cache))
print(cache)
print_coins(coins, amt, cache)
#callgraph.render("coinchange_dyn.png")

