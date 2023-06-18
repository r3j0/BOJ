import sys
input = sys.stdin.readline

test = int(input().rstrip())
for t in range(test):
    string = input().rstrip()
    left_stack = []
    right_stack = []
    for s in string:
        if s == '<':
            if len(left_stack) != 0:
                right_stack.append(left_stack.pop())
        elif s == '>':
            if len(right_stack) != 0:
                left_stack.append(right_stack.pop())
        elif s == '-':
            if len(left_stack) != 0:
                left_stack.pop()
        else:
            left_stack.append(s)
    
    while right_stack:
        left_stack.append(right_stack.pop())
    
    print(''.join(left_stack))