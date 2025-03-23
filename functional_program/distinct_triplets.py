def find_triplets(arr, n):
    triplets = []
    count = 0
    
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                        count += 1
    
    print(count)
    for triplet in triplets:
        print(*triplet)

n = int(input())
arr = list(map(int, input().split()))


find_triplets(arr, n)