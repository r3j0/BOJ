import sys
input = sys.stdin.readline

yeondu = input().rstrip()
string = 'LOVE'
n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(input().rstrip())


max_value = -1
max_name = ""

for a in arr:
    now = 1
    for i in range(3):
        for j in range(i+1,4):
            now *= (yeondu.count(string[i]) + a.count(string[i])) + (yeondu.count(string[j]) + a.count(string[j]))
    now %= 100

    if now > max_value:
        max_value = now
        max_name = a
    elif now == max_value:
        if a == min(max_name, a):
            max_value = now
            max_name = a

print(max_name)
