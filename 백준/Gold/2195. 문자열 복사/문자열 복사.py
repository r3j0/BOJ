import sys
input = sys.stdin.readline

s = str(input().rstrip())[::-1]
p = str(input().rstrip())[::-1]

record = 0
cnt = 0
for i in range(1, len(p)):
    if s.find(p[record:i+1]) == -1:
        cnt += 1
        record = i
    
print(cnt + 1)