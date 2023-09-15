import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))
print(5000 - (arr.count(1)*500 + arr.count(2)*800 + arr.count(3)*1000))