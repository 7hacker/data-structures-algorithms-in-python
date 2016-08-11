'''
Maximize stealing cakes, in a bag of capacity C, where cakes are tuples of weight,profit
'''
import sys
from rcviz import callgraph, viz

def iterative_thief(cake_tuples, capacity, cache):
	for i in range(1, len(cache)):
		maxProfit = -sys.maxint -1
		for cake in cake_tuples:
			if cake[0] <= i and i-cake[0] >= 0:
				profit = cake[1] + cache[i-cake[0]]
				if profit > maxProfit:
					maxProfit = profit
		cache[i] = maxProfit
	return cache[-1]

@viz
def max_duffel_bag_value_dyn(cake_tuples, capacity, cache):
	if capacity == 0:
		return cache[0]
	if capacity < 0:
		return -sys.maxint -1
	else:
		if cache[capacity] is None:
			maxProfit = -sys.maxint -1
			for cake in cake_tuples:
				profit = cake[1] + max_duffel_bag_value_dyn(cake_tuples, capacity-cake[0],cache)
				if profit > maxProfit:
					maxProfit = profit
			cache[capacity] = maxProfit
			#max_duffel_bag_value.track(maxProfit=maxProfit)
		return cache[capacity]

@viz
def max_duffel_bag_value(cake_tuples, capacity):
	if capacity == 0:
		return 0
	if capacity < 0:
		return -sys.maxint -1
	else:
		maxProfit = -sys.maxint -1
		for cake in cake_tuples:
			profit = cake[1] + max_duffel_bag_value(cake_tuples, capacity-cake[0])
			if profit > maxProfit:
				maxProfit = profit
		max_duffel_bag_value.track(maxProfit=maxProfit)
		return maxProfit




cakes = [(7, 160), (3, 90), (2, 15)]
capacity = 20
cache_size = capacity+1
cache = [None] * cache_size
cache[0] = 0
print(cache)
#print(max_duffel_bag_value(cakes, capacity))
#print(max_duffel_bag_value_dyn(cakes, capacity, cache))
print(iterative_thief(cakes, capacity, cache))
print(cache)
#callgraph.render("cakethief_dyn.png")
