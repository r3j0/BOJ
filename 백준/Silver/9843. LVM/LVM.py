import sys
input = sys.stdin.readline

n = int(input().rstrip())
order = []
stack = []
reg = 0
for i in range(n):
    command = input().rstrip()
    order.append(command)

now_in = 0
while now_in < n:
    command = list(order[now_in].split())

    if command[0] == 'PUSH':
        stack.append(int(command[1]))
    elif command[0] == 'STORE':
        reg = stack.pop()
    elif command[0] == 'LOAD':
        stack.append(reg)
    elif command[0] == 'PLUS':
        stack.append(stack.pop() + stack.pop())
    elif command[0] == 'TIMES':
        stack.append(stack.pop() * stack.pop())
    elif command[0] == 'IFZERO':
        tmp = stack.pop()
        if tmp == 0: now_in = int(command[1]) - 1
    elif command[0] == 'DONE':
        print(stack[-1])
        break

    now_in += 1