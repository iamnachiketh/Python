import math

def euclidean_distance(x, y):
    distance = math.sqrt(x**2 + y**2)
    print(distance)

x, y = map(int, input().split())

euclidean_distance(x, y)
