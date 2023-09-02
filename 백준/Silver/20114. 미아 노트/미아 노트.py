import sys
input = sys.stdin.readline

n, h, w = map(int, input().rstrip().split())
result = ['?' for _ in range(n)]
for _ in range(h):
    string = input().rstrip()

    for i in range(n):
        for j in range(w):
            if string[i*w+j] != '?':
                result[i] = string[i*w+j]

print(''.join(result))