import sys
input = sys.stdin.readline

wArr = []
for _ in range(10): wArr.append(int(input().rstrip()))

kArr = []
for _ in range(10): kArr.append(int(input().rstrip()))

wArr.sort()
kArr.sort()

print(wArr[-1] + wArr[-2] + wArr[-3], kArr[-1] + kArr[-2] + kArr[-3])