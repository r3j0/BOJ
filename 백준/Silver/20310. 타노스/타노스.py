import sys
input = sys.stdin.readline

string = list(input().rstrip())
# 가장 앞에 있는 1 지우기. 가장 뒤에 있는 0 지우기
one_count = string.count('1')//2
cnt = 0
idx = 0
while cnt != one_count:
    if string[idx] == '1':
        del string[idx]
        cnt += 1
    else:
        idx += 1
zero_count = string.count('0')//2
cnt = 0
idx = len(string)-1
while cnt != zero_count:
    if string[idx] == '0':
        del string[idx]
        cnt += 1
    idx -= 1

print(''.join(string))