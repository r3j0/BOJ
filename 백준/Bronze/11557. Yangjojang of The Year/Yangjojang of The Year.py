import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    maxs = 0
    maxname = 0
    for i in range(n):
        name, num = input().rstrip().split()
        num = int(num)
        if i == 0:
            maxs = num
            maxname = name
        else:
            if maxs < num:
                maxs = num
                maxname = name
    
    print(maxname)