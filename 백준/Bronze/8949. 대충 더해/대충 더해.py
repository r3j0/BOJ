import sys
input = sys.stdin.readline

a, b = input().rstrip().split()

idx = 1
res = []
while idx <= len(a) or idx <= len(b):
    go_a = 0
    if idx <= len(a): go_a = int(a[-idx])
    go_b = 0
    if idx <= len(b): go_b = int(b[-idx])

    res.append(str(go_a+go_b))
    idx += 1

print(''.join(map(str, res[::-1])))