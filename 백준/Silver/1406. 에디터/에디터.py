import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
m = int(input().rstrip())
for _ in range(m):
    order = list(input().rstrip().split())
    if order[0] == 'L':
        if len(left) > 0:
            right.append(left.pop())
    elif order[0] == 'D':
        if len(right) > 0:
            left.append(right.pop())
    elif order[0] == 'B':
        if len(left) > 0:
            left.pop()
    elif order[0] == 'P':
        left.append(order[1])

while len(right) > 0:
    left.append(right.pop())

print(''.join(left))