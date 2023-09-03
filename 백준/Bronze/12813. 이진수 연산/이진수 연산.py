import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

# A & B
for i in range(len(a)):
    if a[i] == b[i] == '1': print('1', end='')
    else: print('0', end='')
print()

# A | B
for i in range(len(a)):
    if a[i] == '1' or b[i] == '1': print('1', end='')
    else: print('0', end='')
print()

# A ^ B
for i in range(len(a)):
    if a[i] != b[i]: print('1', end='')
    else: print('0', end='')
print()

# ~A
for i in a:
    if i == '0': print('1', end='')
    else: print('0', end='')
print()

# ~B
for i in b:
    if i == '0': print('1', end='')
    else: print('0', end='')
print()