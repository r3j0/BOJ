import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

arr = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

idx = 0
now = ""
while idx < len(a) and idx < len(b):
    now += a[idx]
    now += b[idx]
    idx += 1

if idx < len(a):
    now += a[idx:]
if idx < len(b):
    now += b[idx:]

lis = []
for i in now:
    lis.append(arr[ord(i) - ord('A')])
lens = len(lis)
while lens != 2:
    new_lis = []
    for i in range(len(lis) - 1):
        new_lis.append((lis[i] + lis[i+1]) % 10)
    lis = new_lis
    lens = len(lis)

print(''.join(map(str, lis)))