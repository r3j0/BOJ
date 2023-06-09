import sys
input = sys.stdin.readline
a=int(input().rstrip())
b=int(input().rstrip())
result = [b]
if a >= 20: result.append(int(b*0.75) if int(b*0.75) >= 0 else 0)
if a >= 15: result.append(b - 2000 if b - 2000 >= 0 else 0)
if a >= 10: result.append(int(b*0.9) if int(b*0.9) >= 0 else 0)
if a >= 5: result.append(b - 500 if b - 500 >= 0 else 0)
print(min(result))