def wind_chill(t, v):
    if t > 50 or v < 3 or v > 120:
        print("Invalid input: Conditions not met")
    else:
        wc = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
        print(wc)

t, v = map(float, input().split())

wind_chill(t, v)