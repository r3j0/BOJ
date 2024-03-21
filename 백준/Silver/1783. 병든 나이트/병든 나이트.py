import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 이동 방법 4번을 전부 다 소모하기 위해선
# 세로 3칸, 가로 7칸이 필요함
if n >= 3 and m >= 7:
    print(5 + (m - 7))
else:
    if n >= 3:
        print(min(m, 4))
    elif n == 2:
        print(min((m - 1) // 2 + 1, 4))
    else:
        print(1)