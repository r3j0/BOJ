import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

def icansee(a):
    start = a[0] 
    cnt = 1

    for i in range(1, len(a)):
        if start < a[i]:
            start = a[i]
            cnt += 1
    
    return cnt

print(icansee(arr))
arr.reverse()
print(icansee(arr))