a,b=map(int,input().rstrip().split())
arr = []
for i in range(a): arr.append(int(input().rstrip()))
now = b//sum(arr)
for i in arr: print(now*i)