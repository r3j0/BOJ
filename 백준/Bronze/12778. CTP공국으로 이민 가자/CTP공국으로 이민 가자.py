t = int(input())
for _ in range(t):
    arr1 = list(input().rstrip().split())
    arr2 = list(input().rstrip().split())

    for a in arr2:
        if 'A' <= a <= 'Z': print(ord(a) - ord('A') + 1, end=' ')
        else: print(chr(ord('A') - 1 + int(a)), end=' ')
    print()