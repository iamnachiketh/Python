def double_numbers(arr):
    iterator = map(lambda x:x*2, arr)
    for it in iterator:
        print(it)


arr = []

n = int(input("Enter the length of an array: "))

for i in range(n):
    arr.append(int(input("Enter the number: ")))

double_numbers(arr)