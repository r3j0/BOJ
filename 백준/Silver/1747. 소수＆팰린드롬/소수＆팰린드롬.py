import sys
input = sys.stdin.readline

cha = [0 for _ in range(1003002)]
cha[0] = 1
cha[1] = 1

for i in range(2, 1003002):
    if cha[i] == 0:
        for j in range(2*i, 1003002, i):
            cha[j] = 1

n = int(input())

while (not (cha[n] == 0 and str(n)[:len(str(n))//2] == str(n)[-1:-(len(str(n))//2 + 1):-1])): 
    n += 1

print(n)