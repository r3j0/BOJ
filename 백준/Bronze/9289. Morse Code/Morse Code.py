mos = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
    'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'
}
mos = dict(zip(mos.values(), mos.keys()))

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    result = ""
    arr = list(input().rstrip().split())
    for a in arr:
        result += mos[a]
    print('Case %d:'%i, result)