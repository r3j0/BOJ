import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = {}
for _ in range(n):
    name, num = input().rstrip().split()
    if dic.get(name): dic[name] += int(num)
    else: dic[name] = int(num)

done = 0
for k, v in dic.items():
    if dic[k] == 5:
        print('YES')
        done = 1
        break

if done == 0: print('NO')