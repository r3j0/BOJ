# 34704 : 크기가 4인 박스
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

first = arr.count(4) + arr.count(3) + (arr.count(2) // 2 + (1 if arr.count(2) % 2 else 0))
last_one = max(0, arr.count(1) - arr.count(3) - ((arr.count(2) % 2) * 2))
print(first + last_one // 4 + (1 if last_one % 4 else 0))