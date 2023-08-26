import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    stringArr = list(input().rstrip().split())
    stringArr.reverse()

    print(('Case #%d: '%i) + ' '.join(stringArr))
