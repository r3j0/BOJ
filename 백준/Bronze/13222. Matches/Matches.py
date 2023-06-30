a,b,c=map(int,input().rstrip().split())
for _ in range(a):
    d = int(input().rstrip())
    if b**2+c**2 >= d**2: print('YES')
    else: print('NO')