n = int(input())
count = 0
for _ in range(n):
    coupon = input()
    if int(coupon[2:]) <= 90: count += 1
print(count)