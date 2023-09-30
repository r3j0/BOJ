import sys
input = sys.stdin.readline

n = int(input().rstrip())
sum_value = 0
for _ in range(n):
    tmp = input().rstrip()
    sum_value += int(tmp[:-1])**int(tmp[-1])
print(sum_value)