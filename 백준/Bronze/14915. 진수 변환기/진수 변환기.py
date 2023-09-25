import sys
input = sys.stdin.readline

def convert(now, mode):
    if now // mode == 0:
        if now >= 10: return chr((now % mode - 10) + ord('A'))
        else: return chr((now % mode) + ord('0'))
    if now % mode >= 10:
        return convert(now // mode, mode) + chr((now % mode - 10) + ord('A'))
    else:
        return convert(now // mode, mode) + chr((now % mode) + ord('0'))


m, n = map(int, input().rstrip().split())
print(convert(m, n))