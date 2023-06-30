import sys
input = sys.stdin.readline

string = input().rstrip()

alphabet = [{chr(i+ord('a')):0 for i in range(26)} for _ in range(len(string)+1)]

for i in range(len(string)+1):
    if i == 0: continue
    alphabet[i] = dict(alphabet[i-1])
    alphabet[i][string[i-1]] += 1

q = int(input().rstrip())

for _ in range(q):
    a, l, r = input().rstrip().split()
    l = int(l)
    r = int(r)

    print(alphabet[r+1][a] - alphabet[l][a])