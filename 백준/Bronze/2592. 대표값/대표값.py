import sys
input = sys.stdin.readline

arr = []
for _ in range(10):
    arr.append(int(input().rstrip()))

print(int(sum(arr)/10))

max_num = 0
max_cnt = 0
for i in arr:
    if arr.count(i) > max_cnt:
        max_cnt = arr.count(i)
        max_num = i

print(max_num)