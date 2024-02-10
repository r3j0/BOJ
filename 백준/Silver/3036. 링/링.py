import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
for i in range(1, n):
    now = gcd(arr[0], arr[i])
    print('%d/%d'%(arr[0]//now, arr[i]//now))