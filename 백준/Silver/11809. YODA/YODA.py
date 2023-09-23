import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

a = ((max(len(a), len(b)) - len(a)) * '0') + a
b = ((max(len(a), len(b)) - len(b)) * '0') + b

stack_a = []
stack_b = []

for i in range(len(a) - 1, -1, -1):
    if a[i] > b[i]:
        stack_a.append(a[i])
    elif a[i] < b[i]:
        stack_b.append(b[i])
    else:
        stack_a.append(a[i])
        stack_b.append(b[i])

res_a = ''.join(map(str, stack_a[::-1]))
res_b = ''.join(map(str, stack_b[::-1]))
if res_a == '': print('YODA')
else: print(int(res_a))
if res_b == '': print('YODA')
else: print(int(res_b))