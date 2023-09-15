import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

record = 0
cnt = 0
for i in range(1, len(p)):
    if s.find(p[record:i+1]) == -1:
        cnt += 1
        record = i
    
print(cnt + 1)