import sys
input = sys.stdin.readline

arr = []
for _ in range(15):
    a = list(input().rstrip())
    arr.extend(a)

if arr.count('w') > 0: print('chunbae')
elif arr.count('b') > 0: print('nabi')
else: print('yeongcheol')