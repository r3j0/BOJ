import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    want = list(map(int, input().rstrip().split()))

    day = 1

    while n - sum(want) >= 0:
        now_want = [0 for _ in range(6)]
        for i in range(6):
            leftIdx = (i - 1) if i - 1 >= 0 else (i - 1 + 6)
            rightIdx = ((i + 1) % 6)
            oppoIdx = ((i + 3) % 6)
            now_want[i] = want[i] + want[leftIdx] + want[rightIdx] + want[oppoIdx]

        want = now_want
        day += 1

    print(day)