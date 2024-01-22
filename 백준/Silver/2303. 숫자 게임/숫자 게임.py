import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = 0
res_num = 0
for i in range(n):
    arr = list(map(int, input().rstrip().split()))
    for a in range(3):
        for b in range(a+1, 4):
            for c in range(b+1, 5):
                if res_num <= (arr[a] + arr[b] + arr[c]) % 10:
                    res = i
                    res_num = (arr[a] + arr[b] + arr[c]) % 10

print(res + 1)
