import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    height, weight = map(int, input().rstrip().split())
    bmi = weight / ((height / 100)**2)
    if height < 140.1: print(6)
    elif height < 146: print(5)
    elif height < 159: print(4)
    elif height < 161:
        if bmi >= 16 and bmi < 35: print(3)
        else: print(4)
    elif height < 204:
        if bmi < 16 or bmi >= 35: print(4)
        elif bmi < 18.5 or bmi >= 30: print(3)
        elif bmi < 20 or bmi >= 25: print(2)
        else: print(1)
    else: print(4)