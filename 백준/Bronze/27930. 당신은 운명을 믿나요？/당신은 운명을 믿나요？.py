import sys
input = sys.stdin.readline

string = input().rstrip()
s1 = 'KOREA'
s1_idx = 0
s2 = 'YONSEI'
s2_idx = 0

for s in string:
    if s1[s1_idx] == s: s1_idx += 1
    if s2[s2_idx] == s: s2_idx += 1

    if s1_idx == 5: 
        print(s1)
        break
    if s2_idx == 6:
        print(s2)
        break