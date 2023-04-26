n = int(input())

print('int a;')
print('int *ptr = &a;')
for i in range(2, n+1):
    print('int ', end='')
    for j in range(i):
        print('*', end='')
    print('ptr',end='')
    print(j+1,end='')
    print(' = &ptr', end='')
    if i != 2: print(str(j)+';')
    else: print(';')
        