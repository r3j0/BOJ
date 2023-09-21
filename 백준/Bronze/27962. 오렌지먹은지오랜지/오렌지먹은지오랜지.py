import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

def yusa(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]: cnt += 1
    
    if cnt == 1: return 1
    else: return 0

done = 0
for length in range(1, len(string)+1):
    if yusa(string[:length], string[-length:]):
        done = 1
        break
print('YES' if done == 1 else 'NO')