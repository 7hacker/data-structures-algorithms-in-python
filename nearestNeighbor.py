'''
http://stackoverflow.com/questions/20398799/find-k-nearest-points-to-point-p-in-2-dimensional-plane
'''

def distance(v1,v2): 
    return sum([(x-y)**2 for (x,y) in zip(v1,v2)])**(0.5)

print(distance([2,3], [3,4]))