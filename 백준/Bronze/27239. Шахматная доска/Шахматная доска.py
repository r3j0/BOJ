n = int(input())
print(chr(ord('a') + (n - 1) % 8), end='')
print((n - 1) // 8 + 1)