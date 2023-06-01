import sys      
input = sys.stdin.readline

grundy = [-1] * 2001
grundy[0] = 0
grundy[1] = 0
grundy[2] = 1

def mex(l):
    l = sorted(l)
    for i in range(len(l)):
        if i != l[i]:
            return i
    return len(l)

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

for i in range(3, max(arr)+1):
    s = []
    for k in range(1, i):
        first = k if (i // k) % 2 == 1 else 0
        second = i % k
        s.append((first, second))
    
    sr = set()
    for ss in s:
        sr.add(grundy[ss[0]] ^ grundy[ss[1]])

    grundy[i] = mex(sr)

result = 0
for a in arr:
    result ^= grundy[a]
if result == 0: print('Second')
else: print('First')