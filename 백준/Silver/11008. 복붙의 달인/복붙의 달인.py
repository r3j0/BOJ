import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    s, p = input().rstrip().split()
    idx = 0
    cnt_clip = 0
    cnt = 0
    while idx < len(s):
        if idx + len(p) - 1 < len(s) and s[idx:idx+len(p)] == p:
            idx += len(p)
            cnt_clip += 1
        else:
            idx += 1
            cnt += 1
    
    print(cnt_clip + cnt)