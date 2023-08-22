import sys
input = sys.stdin.readline

original = input().rstrip()
source = input().rstrip()

idx = 0
cnt = 0
while idx < len(original):
    if original[idx] == source[0]:
        if original[idx:idx+len(source)] == source:
            cnt += 1
            idx += len(source) - 1
    
    idx += 1
print(cnt)