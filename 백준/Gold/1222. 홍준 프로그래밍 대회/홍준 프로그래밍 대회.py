# 1222 : 홍준 프로그래밍 대회
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
joined = [0 for _ in range(2_000_001)]
for a in arr: joined[a] += 1

# arr 의 약수들 중
# (약수 등장 횟수) * 약수 의 최댓값
# 이때 약수 등장 횟수는 최소 2이여야 함

# k * (k의 배수인 학교 수)

ans = n
end = max(arr)

for i in range(2, end+1):
    cnt = 0
    j = 1
    while i * j <= end:
        cnt += joined[i * j]
        j += 1
    
    if cnt > 1:
        ans = max(ans, cnt * i)

print(ans)