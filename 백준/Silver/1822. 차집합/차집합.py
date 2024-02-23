import sys
input = sys.stdin.readline

na, nb = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

S = set()
for i in a: S.add(i)
for i in b:
    if i in S: S.remove(i)

print(len(S))
S = list(sorted(list(S)))
print(" ".join(map(str, S)))