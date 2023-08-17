import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

def solve(a):
    for k in range(1, len(str(min(a))) + 1):
        for i in range(len(a)):
            for j in range(len(a)):
                if str(a[i])[:k] == str(a[j])[-k:]:
                    print(i + 1, j + 1)
                    return

    print(-1)

solve(arr)