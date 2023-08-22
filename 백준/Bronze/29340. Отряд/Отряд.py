a = list(input().rstrip())
b = list(input().rstrip())

for i in range(len(a)):
    print(max(int(a[i]), int(b[i])), end='')