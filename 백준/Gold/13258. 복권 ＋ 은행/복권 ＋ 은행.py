import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
j = int(input().rstrip())
c = int(input().rstrip())

e = arr[0]+(float(arr[0]/sum(arr))*j*c)
print(e)