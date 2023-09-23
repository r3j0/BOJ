import sys
input = sys.stdin.readline

string = input().rstrip()
cnt = 0
sums = 0
for i in range(1, len(string)):
    if 'A' <= string[i] <= 'Z':
        sums += 3 - (cnt % 4)
        cnt = 0
    else:
        cnt += 1
print(sums)