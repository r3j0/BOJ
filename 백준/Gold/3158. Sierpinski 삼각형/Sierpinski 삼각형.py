import sys
input = sys.stdin.readline

a = input().rstrip()
if a[-1] == '4':
    print(a[:-1] + '1')
    print(a[:-1] + '2')
    print(a[:-1] + '3')
else:
    for i in range(len(a)-1, 0, -1):
        flag = True
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                flag = False
                break
        if flag: print(a[:i] + '4')