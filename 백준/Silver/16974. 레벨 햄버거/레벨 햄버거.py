import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())

burn = [0 for _ in range(n+1)]
paty = [0 for _ in range(n+1)]

burn[0] = 0
paty[0] = 1
for i in range(1, n+1):
    burn[i] = 2 * burn[i-1] + 2
    paty[i] = 2 * paty[i-1] + 1

def hamburger(left, num):
    global burn
    global paty
    global x

    if num == 0:
        if left > x:
            return 0
        
        return 1
    else:
        now_left = 1
        now_paty = 0

        if left + now_left >= x:
            return 0

        res = hamburger(left + now_left, num - 1)

        if left + now_left + burn[num - 1] + paty[num - 1] > x:
            return res
        elif left + now_left + burn[num - 1] + paty[num - 1] == x:
            return paty[num - 1]

        now_left += burn[num - 1] + paty[num - 1] + 1
        now_paty += paty[num - 1] + 1

        if left + now_left == x:
            return now_paty

        if left + now_left + burn[num - 1] + paty[num - 1] > x:
            return now_paty + hamburger(left + now_left, num - 1)
        else:
            return now_paty + paty[num - 1]

print(hamburger(0, n))  