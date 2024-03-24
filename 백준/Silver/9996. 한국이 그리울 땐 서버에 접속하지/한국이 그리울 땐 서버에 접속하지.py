import sys
input = sys.stdin.readline

n = int(input().rstrip())
pattern = list(input().rstrip().split('*'))
for _ in range(n):
    string = input().rstrip()
    if string[:len(pattern[0])] == pattern[0] and string[len(string)-len(pattern[1]):] == pattern[1] and len(string) >= len(pattern[0]) + len(pattern[1]): print('DA')
    else: print('NE')