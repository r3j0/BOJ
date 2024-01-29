import sys
input = sys.stdin.readline

t = 0
while True:
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 0: break
    if t == 0: t = 1
    else: print()

    n = arr[0]
    sets = arr[1:]
    sets.sort()

    for n1 in range(n):
        for n2 in range(n1 + 1, n):
            for n3 in range(n2 + 1, n):
                for n4 in range(n3 + 1, n):
                    for n5 in range(n4 + 1, n):
                        for n6 in range(n5 + 1, n):
                            print(sets[n1], sets[n2], sets[n3], sets[n4], sets[n5], sets[n6])
