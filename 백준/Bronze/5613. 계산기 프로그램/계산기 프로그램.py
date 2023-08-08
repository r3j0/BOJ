start = 0
now = 0
mode = 0
while True:
    n = input().rstrip()
    if start == 0:
        start = 1
        now = int(n)
    else:
        if n in ['+', '-', '*', '/']:
            mode = n
        elif n == '=':
            print(now)
            break
        else:
            if mode == '+':
                now = now + int(n)
                mode = 0
            elif mode == '-':
                now = now - int(n)
                mode = 0
            elif mode == '*':
                now = now * int(n)
                mode = 0
            else:
                now = now // int(n)
                mode = 0