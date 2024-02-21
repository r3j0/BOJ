import sys
input = sys.stdin.readline

n1, n2 = map(int, input().rstrip().split())
arr1 = list(input().rstrip())
arr2 = list(input().rstrip())
t = int(input().rstrip())

now = t
for i in range(n1):
    arr2.insert(max(0, min(n2, now)), arr1[i])
    now -= 1

print(''.join(arr2))