def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()

m = int(input("Enter the number of columns: "))
n = int(input("Enter the number of rows: "))


arr = [[0] * n for _ in range(m)]  


for i in range(m):
    for j in range(n):
        arr[i][j] = input(f"Enter the number at position ({i}, {j}): ")


print_matrix(arr)
