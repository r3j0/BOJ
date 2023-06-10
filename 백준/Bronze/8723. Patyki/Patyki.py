# 0 - Byte가 직각 삼각형도 정삼각형도 만들 수 없는 경우 1 - Byte가 직각 삼각형만 만들 수 있는 경우 2 - Byte가 정삼각형만 만들 수 있는 경우
import sys
input = sys.stdin.readline

stick = sorted(map(int, input().rstrip().split()))

if stick[0]**2 + stick[1]**2 == stick[2]**2: print(1)
elif stick[0] == stick[1] == stick[2]: print(2)
else: print(0)