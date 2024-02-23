import sys
input = sys.stdin.readline

string = list(input().rstrip().split())

stack = []
res = 0
for s in string:
    if s == '[': stack.append(0)
    elif '1' <= s[0] <= '9': # 정수
        stack[-1] += 8
    elif 'a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z': # 문자열
        stack[-1] += len(s) + 12
    elif s == ']':
        if len(stack) == 1:
            res = stack[-1] + 8
        else:
            stack[-2] += stack[-1] + 8
        stack.pop()
print(res)
