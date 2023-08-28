import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    cnt = 0
    while n != 6174:
        n = '%04d'%n
        big = ''.join(list(sorted(list(n)))[::-1])
        small = ''.join(list(sorted(list(n))))
        n = int(big) - int(small)
        cnt += 1

    print(cnt)