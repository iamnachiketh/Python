import math

def quadratic_roots(a, b, c):
    d = b**2 - 4*a*c
    
    if d < 0:
        print("No Real Roots")
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print(root1, root2)

a, b, c = map(int, input().split())

quadratic_roots(a, b, c)