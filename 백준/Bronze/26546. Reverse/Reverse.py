t = int(input())
for _ in range(t):
    s, a, b = input().split()
    a = int(a)
    b = int(b)
    for i in range(len(s)):
        if i >= a and b > i: 
            continue
        print(s[i], end='')
    print()