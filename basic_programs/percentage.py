# Percentage of heads vs tails

import random
def probability_calculate(n, hcount, tcount):
    for i in range(n):
        num = random.random()
        if num > 0.5 : tcount = tcount + 1
        else: hcount = hcount + 1
    return [hcount, tcount]

n = int(input("Enter the Number of times to flip a coin: "))
if(n < 0):
    print("Enter the a positive number")
else:
    res = probability_calculate(n, 0, 0)
    print(f"Percentage of heads: {(res[0]/n)*100}\n Percentage of tails: {(res[1]/n)*100}")
