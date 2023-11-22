import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n <= 99: print(n)
else:
    count = 99
    for i in range(100, min(1000, n + 1)):
        n1 = i // 100
        n2 = i % 100 // 10
        n3 = i % 10

        if n1 - n2 == n2 - n3: count += 1
    print(count)