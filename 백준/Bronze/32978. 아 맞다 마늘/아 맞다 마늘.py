n = int(input())
arrA = list(input().split())
arrB = list(input().split())
for i in range(len(arrA)):
    if arrB.count(arrA[i]) == 0:
        print(arrA[i])
        break