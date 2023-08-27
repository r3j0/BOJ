import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    aArr = list(map(int, input().rstrip().split()))
    bArr = list(map(int, input().rstrip().split()))

    aScore = aArr[0] + aArr[1] * 2 + aArr[2] * 3 + aArr[3] * 3 + aArr[4] * 4 + aArr[5] * 10
    bScore = bArr[0] + bArr[1] * 2 + bArr[2] * 2 + bArr[3] * 2 + bArr[4] * 3 + bArr[5] * 5 + bArr[6] * 10

    print('Battle %d: '%i, end='')

    if aScore == bScore:
        print('No victor on this battle field')
    elif aScore > bScore:
        print('Good triumphs over Evil')
    else:
        print('Evil eradicates all trace of Good')