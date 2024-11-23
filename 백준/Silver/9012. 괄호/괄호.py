def isPString(string):
    now = 0 # 현재 여는 괄호 수
    now2 = 0 # [
    for s in string:
        if s == '(': now += 1
        elif s == ')':
            if now == 0: # 여는 괄호가 부족
                return -1
            now -= 1
        elif s == '[': now2 += 1
        elif s == ']':
            if now2 == 0:
                return -1
            now2 -= 1
        
    if now > 0: # 여는 괄호가 남음
        return -1
    if now2 > 0:
        return -1
    return 1

t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    print('YES' if isPString(s) == 1 else 'NO')