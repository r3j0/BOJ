import sys
input = sys.stdin.readline

key = input().rstrip()
n = int(input())

result = 0
for _ in range(n):
    string = input().rstrip()
    string += string

    if string.count(key) > 0: result += 1

print(result)