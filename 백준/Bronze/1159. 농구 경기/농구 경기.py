import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    string = input().rstrip()

    if dic.get(string[0]): dic[string[0]] += 1
    else: dic[string[0]] = 1

arr = []
for k, v in dic.items():
    if v >= 5: arr.append(k)

if len(arr) > 0:
    arr.sort()
    print(''.join(arr))
else:
    print("PREDAJA")