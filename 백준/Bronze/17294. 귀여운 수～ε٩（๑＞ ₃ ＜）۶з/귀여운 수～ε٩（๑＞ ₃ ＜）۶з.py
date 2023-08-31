import sys
input = sys.stdin.readline

k = list(input().rstrip())
arr = []
for i in range(len(k) - 1):
    arr.append((ord(k[i+1]) - ord('0')) - (ord(k[i]) - ord('0')))
result = 1
if len(arr) > 0 and max(arr) != min(arr):
    result = 0

print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!' if result == 1 else '흥칫뿡!! <(￣ ﹌ ￣)>')