n = int(input())
a = input()
b = input()
if n % 2 == 1:
    done = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            done = 1
            break
    if done == 1: print('Deletion failed')
    else: print('Deletion succeeded')
else:
    done = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            done = 1
            break
    if done == 1: print('Deletion failed')
    else: print('Deletion succeeded')