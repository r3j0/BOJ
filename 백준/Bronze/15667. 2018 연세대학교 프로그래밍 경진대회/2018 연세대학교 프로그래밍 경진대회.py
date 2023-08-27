import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 대형 1개 -> 중형 k 개 + 1 (k+1) -> 소형 k*k개 (k^2+k+1)
# 만약 1뺀 값이 연속된 수의 곱이라면 거기서 작은 수 출력

now = 1
while True:
    if now * (now + 1) == n - 1:
        print(now)
        break
    now += 1