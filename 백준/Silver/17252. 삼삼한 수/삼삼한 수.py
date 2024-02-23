import sys
input = sys.stdin.readline

n = int(input().rstrip())
done = False
def backtracking(now, start):
    global n
    global done
    if now == n and n != 0:
        done = True
        return
    if now > n:
        return
    
    for i in range(start, 21):
        backtracking(now + 3**i, i+1)

backtracking(0, 0)
print('YES' if done else 'NO')