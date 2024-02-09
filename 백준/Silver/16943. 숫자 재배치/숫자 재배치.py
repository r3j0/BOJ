import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
a_list = list(str(a))
b_list = list(str(b))
n = len(a_list)

result = -1
def backtracking(vis, now):
    global result
    if vis == (1 << n) - 1:
        a_res = int(''.join(now))
        if a_res < b:
            result = max(result, a_res)
        return
    
    for i in range(n):
        if vis == 0 and a_list[i] == '0': continue
        if ((vis & (1 << (n - 1 - i))) >> (n - 1 - i)) == 0:
            vis |= (1 << (n - 1 - i))
            backtracking(vis, now + [a_list[i]])
            vis ^= (1 << (n - 1 - i))

backtracking(0, [])
print(result)