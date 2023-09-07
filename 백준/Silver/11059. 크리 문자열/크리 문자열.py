import sys
input = sys.stdin.readline

s = input().rstrip()
done = 0
for length in range((len(s)//2)*2, 1, -2):
    for start in range(0, len(s) - length + 1):
        now = s[start:start+length]
        left = now[:(length//2)]
        right = now[(length//2):]

        if sum(list(map(int, list(left)))) == sum(list(map(int, list(right)))):
            print(length)
            done = 1
            break
    if done == 1: break

if done == 0: print(0)