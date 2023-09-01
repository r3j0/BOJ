import sys
input = sys.stdin.readline

s1, s2, s3 = map(int, input().rstrip().split())
su = {}

for n1 in range(1, s1+1):
    for n2 in range(1, s2+1):
        for n3 in range(1, s3+1):
            if su.get(n1+n2+n3): su[n1+n2+n3] += 1
            else: su[n1+n2+n3] = 1

arr = list(su.items())
arr.sort(key=lambda x:(-x[1], x[0]))
print(arr[0][0])