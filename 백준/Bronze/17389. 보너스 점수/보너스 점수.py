import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
result = 0
bonus = 0
for i in range(n):
    if string[i] == 'O':
        result += i + 1
        result += bonus
        bonus += 1
    else:
        bonus = 0
print(result)