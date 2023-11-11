n = int(input())
cnt = 0
col = [-1] * n

def invalid(i):
    for zz in range(i):
        if col[i] == col[zz] or abs(col[i] - col[zz]) == abs(i - zz):
            return False
    return True

def queen(i):
    global cnt
    if i == n:
        cnt += 1
        return
    
    for row in range(n):
        col[i] = row
        if invalid(i):
            queen(i + 1)

queen(0)
print(cnt)