import sys
input = sys.stdin.readline

while True:
    a, b = input().rstrip().split()
    if a == b == '0': break

    sa = list(map(int, list((((len(a) * len(b)) - len(a))*'0') + a)))
    sb = list(map(int, list((((len(a) * len(b)) - len(b))*'0') + b)))

    cnt = 0
    for i in range(len(sa) - 1, -1, -1):
        if sa[i] + sb[i] >= 10:
            sa[i-1] += ((sa[i]) + (sb[i])) // 10
            cnt += 1
    print(cnt)