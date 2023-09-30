import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '#': break

    sums = 0
    for i in range(len(string)):
        if string[i] == ' ': continue
        sums += (i + 1) * (ord(string[i]) - ord('A') + 1)
    print(sums)