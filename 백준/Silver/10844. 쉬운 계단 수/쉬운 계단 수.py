import sys
input = sys.stdin.readline

n = int(input().rstrip())
digits = [1 for _ in range(10)]
digits[0] = 0
for _ in range(n - 1):
    new_digits = [0 for _ in range(10)]
    for i in range(10):
        if i > 0:
            new_digits[i] += digits[i - 1]
        if i < 9:
            new_digits[i] += digits[i + 1]
    digits = new_digits

print(sum(digits) % 1000000000)