import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    first = arr[0]
    result = [first - 1]
    for a in range(1, len(arr)-1):
        result.append(arr[a] * first)
        first -= 1
    
    print('Case %d: '%(i+1), end='')
    print(' '.join(map(str, result)))