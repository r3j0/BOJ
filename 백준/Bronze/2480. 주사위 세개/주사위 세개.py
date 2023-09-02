import sys
input = sys.stdin.readline

arr = list(sorted(map(int, input().rstrip().split())))

if arr.count(arr[0]) == 3: print(10000+arr[0]*1000)
elif arr[0] == arr[1] or arr[1] == arr[2]: print(1000+arr[1]*100)
else: print(arr[2]*100)