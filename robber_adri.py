from rcviz import callgraph, viz


def robber_iterative(houses, cache):
	last_house = len(houses) - 1
	second_last_house = last_house - 1
	third_last_house = second_last_house - 1

	best = max(houses[last_house], houses[second_last_house])

	cache[last_house] = best
	cache[second_last_house] = best

	for i in range(third_last_house, -1, -1):
		cache[i] = max(houses[i] + cache[i+2], cache[i+1])

	return cache[0]


@viz
def robber(houses, index, cache):
	if index >= len(houses):
		if cache[index] == -1:
			cache[index] = 0
		else:
			cachehit = "Cache hit!"
			robber.track(cache_hit = cachehit)
		return cache[index]
	else:
		if cache[index] == -1:
			stolen = houses[index] + robber(houses, index+2, cache)
			notStolen = robber(houses, index+1, cache)
			robber.track(stolen = stolen)
			robber.track(notStolen = notStolen)
			cache[index] = max(stolen, notStolen)
		else:
			cachehit = "Cache hit!"
			robber.track(cache_hit = cachehit)
		return cache[index]


houses = [2, 3, 5, 6]

cache_size = len(houses) + 2
cache = [-1] * cache_size

print(cache)
print(robber_iterative(houses, cache))
print(cache)

#callgraph.render("robber_adri.png")
