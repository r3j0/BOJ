import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '#': break

    alpha = [0 for _ in range(26)]
    for s in string:
        if 'A' <= s <= 'Z': alpha[ord(s) - ord('A')] = 1
        elif 'a' <= s <= 'z': alpha[ord(s) - ord('a')] = 1
    
    print(sum(alpha))