import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
a_sameidx = -1
b_sameidx = -1
for i in range(len(a)):
    if a_sameidx != -1: break
    for j in range(len(b)):
        if a_sameidx != -1: break
        if a[i] == b[j]:
            a_sameidx = i
            b_sameidx = j

for i in range(len(b)):
    if b_sameidx == i: print(a)
    else:
        for j in range(len(a)):
            if a_sameidx != j: print('.', end='')
            else: print(b[i], end='')
        print()