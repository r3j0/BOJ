import sys
input = sys.stdin.readline

b, c, d = map(int, input().rstrip().split())
burger = list(map(int, input().rstrip().split()))
burger.sort(reverse=True)
side = list(map(int, input().rstrip().split()))
side.sort(reverse=True)
drink = list(map(int, input().rstrip().split()))
drink.sort(reverse=True)

print(sum(burger) + sum(side) + sum(drink))

idx = 0
disc = 0
while idx < b and idx < c and idx < d:
    disc += int((burger[idx] + side[idx] + drink[idx]) * 0.9)
    idx += 1
while idx < b or idx < c or idx < d:
    disc += (burger[idx] if idx < b else 0) + (side[idx] if idx < c else 0) + (drink[idx] if idx < d else 0)
    idx += 1
print(disc)