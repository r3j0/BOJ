import sys
input = sys.stdin.readline

n = int(input().rstrip())
unwash = [i for i in range(n, 0, -1)]
washnotdry = []
washdry = []

while len(washdry) != n:
    a, b = map(int, input().rstrip().split())
    if a == 1:
        for _ in range(b):
            if len(unwash) == 0: break
            washnotdry.append(unwash[-1])
            del unwash[-1]
    else:
        for _ in range(b):
            if len(washnotdry) == 0: break
            washdry.append(washnotdry[-1])
            del washnotdry[-1]

for i in range(n-1, -1, -1): print(washdry[i])