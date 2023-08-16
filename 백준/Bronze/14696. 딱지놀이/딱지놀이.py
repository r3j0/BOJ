import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    aArr = list(map(int, input().rstrip().split()))[1:]
    bArr = list(map(int, input().rstrip().split()))[1:]

    if aArr.count(4) > bArr.count(4): print('A')
    elif aArr.count(4) < bArr.count(4): print('B')
    else:
        if aArr.count(3) > bArr.count(3): print('A')
        elif aArr.count(3) < bArr.count(3): print('B')
        else:
            if aArr.count(2) > bArr.count(2): print('A')
            elif aArr.count(2) < bArr.count(2): print('B')
            else:
                if aArr.count(1) > bArr.count(1): print('A')
                elif aArr.count(1) < bArr.count(1): print('B')
                else: print('D')
