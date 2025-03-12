def prime_factors(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1
    if n > 1:
        print(n)

n = int(input("Enter a number: "))
prime_factors(n)