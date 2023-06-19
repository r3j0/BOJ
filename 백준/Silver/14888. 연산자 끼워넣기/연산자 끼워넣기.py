import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
ope = list(map(int, input().rstrip().split()))

mv = 0
nv = 0
mv_avail = 0
nv_avail = 0

def calc(form):
    now = form[0]
    idx = 1
    while idx < len(form):
        oh = 0
        if form[idx] == '+': now += form[idx + 1]
        elif form[idx] == '-': now -= form[idx + 1]
        elif form[idx] == '*': now *= form[idx + 1]
        elif form[idx] == '/': 
            if now < 0:
                oh = 1
                now *= -1
            now //= form[idx + 1]
            if oh == 1:
                now *= -1
        idx += 2
    
    return now

def backtracking(a, op, r, s):
    global n
    global mv
    global nv
    global mv_avail
    global nv_avail
    if n == s:
        result = calc(r)
        if mv_avail == 0 or mv < result:
            mv_avail = 1
            mv = result
        if nv_avail == 0 or nv > result:
            nv_avail = 1
            nv = result

    for o in range(4):
        if op[o] == 0: continue
        op[o] -= 1
        if o == 0: r.append('+')
        elif o == 1: r.append('-')
        elif o == 2: r.append('*')
        elif o == 3: r.append('/')
        r.append(arr[s])
        s += 1
        backtracking(a, op, r, s)
        s -= 1
        r.pop()
        r.pop()
        op[o] += 1

backtracking(arr, ope, [arr[0]], 1)

print(mv)
print(nv)