def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    print("Transpose matrix")
    for row in transposed:
        print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose(matrix)