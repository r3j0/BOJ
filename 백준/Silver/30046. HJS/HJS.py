import sys
input = sys.stdin.readline

n = int(input().rstrip())
p = input().rstrip()
q = input().rstrip()
r = input().rstrip()

# H, J, S
result = False
for h in range(1, 4):
    for j in range(1, 4):
        if h == j: continue
        for s in range(1, 4):
            if h == s or j == s: continue
            relation = [0, 0, 0]
            for k in range(n):
                p_now = 0
                q_now = 0
                r_now = 0
                if p[k] == 'H': p_now = h
                elif p[k] == 'J': p_now = j
                else: p_now = s
                if q[k] == 'H': q_now = h
                elif q[k] == 'J': q_now = j
                else: q_now = s
                if r[k] == 'H': r_now = h
                elif r[k] == 'J': r_now = j
                else: r_now = s
                if relation[0] == 0 and p_now < q_now: relation[0] = 1
                elif relation[0] == 0 and p_now > q_now: break 
                if relation[1] == 0 and p_now < r_now: relation[1] = 1
                elif relation[1] == 0 and p_now > r_now: break
                if relation[2] == 0 and q_now < r_now: relation[2] = 1
                elif relation[2] == 0 and q_now > r_now: break

            if sum(relation) == 3: 
                result = True
                break
        if result == True: break
    if result == True: break
            

if result == True: print('HJS! HJS! HJS!')
else: print('Hmm...')