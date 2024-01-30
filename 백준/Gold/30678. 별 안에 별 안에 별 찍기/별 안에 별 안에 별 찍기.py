import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [[] for _ in range(5**n)]

def starstar(now, y):
    if now == 0:
        arr[y].append('*')
        return
    
    for k in range(2):
        for _ in range(2):
            for i in range(5**(now-1)):
                arr[(y*(5**(now)))+i+(k*(5**(now-1)))].append(' '*(5**(now-1)))
        starstar(now - 1, y * 5 + k)
        for _ in range(2):
            for i in range(5**(now-1)):
                arr[(y*(5**(now)))+i+(k*(5**(now-1)))].append(' '*(5**(now-1)))
    
    for _ in range(5):
        starstar(now - 1, y * 5 + 2)
    
    for i in range(5**(now-1)):
        arr[(y*(5**(now)))+i+(3*(5**(now-1)))].append(' '*(5**(now-1)))
    for _ in range(3):
        starstar(now - 1, y * 5 + 3)
    for i in range(5**(now-1)):
        arr[(y*(5**(now)))+i+(3*(5**(now-1)))].append(' '*(5**(now-1)))

    for i in range(5**(now-1)):
        arr[(y*(5**(now)))+i+(4*(5**(now-1)))].append(' '*(5**(now-1)))
    starstar(now - 1, y * 5 + 4)
    for i in range(5**(now-1)):
        arr[(y*(5**(now)))+i+(4*(5**(now-1)))].append(' '*(5**(now-1)))
    starstar(now - 1, y * 5 + 4)
    for i in range(5**(now-1)):
        arr[(y*(5**(now)))+i+(4*(5**(now-1)))].append(' '*(5**(now-1)))

starstar(n, 0)

for i in range(5**n): 
    print(''.join(arr[i]))
