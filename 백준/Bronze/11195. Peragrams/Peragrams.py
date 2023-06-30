import sys
input = sys.stdin.readline

string = list(input().rstrip())
alphabet = [0 for _ in range(26)]
for s in range(len(string)):
    alphabet[ord(string[s])-ord('a')] += 1

result = []
for i in range(26):
    if alphabet[i] % 2 == 1: result.append(alphabet[i])

print(0 if len(result) - 1 < 0 else len(result) - 1)