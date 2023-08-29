import sys
input = sys.stdin.readline

s1, s2 = map(int, input().rstrip().split())
sample_cnt = 0
system_cnt = 0
for _ in range(s1):
    a, b = map(int, input().rstrip().split())
    if a == b:
        sample_cnt += 1
for _ in range(s2):
    a, b = map(int, input().rstrip().split())
    if a == b:
        system_cnt += 1

if s1 == sample_cnt and s2 == system_cnt:
    print('Accepted')
elif s1 == sample_cnt and s2 != system_cnt:
    print('Why Wrong!!!')
else:
    print('Wrong Answer')