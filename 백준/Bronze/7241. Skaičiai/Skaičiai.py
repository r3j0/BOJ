arr = list(map(int, input().rstrip().split()))
arr.sort()
res = []
for i in range(3):
    for j in range(3):
        if i == j: continue
        for k in range(3):
            if i == k or k == j: continue
            res.append(str(arr[i]) + str(arr[j]) + str(arr[k]))

print(res.index(input()) + 1)