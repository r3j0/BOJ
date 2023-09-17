import sys
input = sys.stdin.readline

string = ""
for _ in range(4):
    tmp = input().rstrip()
    string += tmp

alpha = [0 for _ in range(26)]
for s in string:
    if 'A' <= s <= 'Z': alpha[ord(s) - ord('A')] += 1
    elif 'a' <= s <= 'z': alpha[ord(s) - ord('a')] += 1

for row in range(max(alpha)):
    now = ""
    for col in range(26):
        if alpha[col] >= max(alpha) - row:
            now += "*"
        else:
            now += " "
        if col != 25: now += " "
    if now.strip() != "": print(now.rstrip())
for i in range(26):
    print(chr(ord('A') + i), end='')
    if i != 25: print(' ', end='')