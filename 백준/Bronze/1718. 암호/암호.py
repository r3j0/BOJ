import sys
input = sys.stdin.readline

original = input().rstrip()
key = input().rstrip()

keyidx = 0

for o in original:
    if o == ' ': print(' ', end='')
    else:
        now = (((ord(o) - ord('a')) - (ord(key[keyidx]) - ord('a') + 1)))
        if now < 0: now += 26

        print(chr(now + ord('a')), end='')
    keyidx = (keyidx + 1) % len(key)
