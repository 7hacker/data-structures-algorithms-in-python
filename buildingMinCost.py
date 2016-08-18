'''
There are N buildings with variable number of floors, and we want to build additional floors so that at least m buildings are of the same height.  Minimize the cost of building the floors.
'''
import sys

def buildingMinCost(buildings, m):
    buildings.sort()
    window = []
    minWindowCost = sys.maxint
    currentWindowCost = 0
    
    #set up window
    for i in xrange(m):
        window.append(buildings[i])

    #compute first window cost
    for i in xrange(m):
        currentWindowCost = currentWindowCost + (window[-1] - window[i])

    #set it to the minWindowCost
    if currentWindowCost < minWindowCost:
        minWindowCost = currentWindowCost

    for i in xrange(m,len(buildings)):
        #drop off the first building
        currentWindowCost = currentWindowCost - (window[-1] - window[0])
        window.pop(0)

        #compute the next delta and add the new building
        nextDelta = buildings[i] - window[-1]
        window.append(buildings[i])

        #compute the new window size
        currentWindowCost = currentWindowCost + (nextDelta * (m-1))
        if currentWindowCost < minWindowCost:
            minWindowCost = currentWindowCost

    return minWindowCost


print(buildingMinCost([10,3,1,5,11,10],3))