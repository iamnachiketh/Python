def reverse_array(arr):
    it = reversed(arr)
    for i in it:
        print(i)

arr = []

n = int(input("Enter the length of an array: "))

for i in range(n):
    arr.append(int(input("Enter the number: ")))

reverse_array(arr)