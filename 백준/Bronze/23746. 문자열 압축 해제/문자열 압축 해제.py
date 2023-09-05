import sys
input = sys.stdin.readline

n = int(input().rstrip())
alpha = {}
for _ in range(n):
    a, b = input().rstrip().split()
    alpha[b] = a

string = input().rstrip()
result = ""

for si in string:
    result += alpha[si]

s, e = map(int, input().rstrip().split())
print(result[s-1:e])