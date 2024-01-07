a, b, c, d = map(int, input().rstrip().split())
ai = 0
bi = 0
ci = 0
cnt = 0
while ai*a <= d:
    bi = 0
    while ai*a + bi*b <= d:
        ci = 0
        while ai*a + bi*b + ci*c <= d:
            if ai*a + bi*b + ci*c == d: 
                cnt += 1
                print(ai, bi, ci)
            ci += 1
        bi += 1
    ai += 1
if cnt == 0: print('impossible')