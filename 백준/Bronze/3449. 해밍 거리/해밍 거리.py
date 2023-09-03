import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a = input().rstrip()
    b = input().rstrip()

    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]: cnt += 1
    
    print('Hamming distance is %d.'%cnt)