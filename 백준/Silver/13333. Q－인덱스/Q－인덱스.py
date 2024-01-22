import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()

# k번 이상 인용된 논문이 k편 이상이고 
# 나머지 n − k 편의 논문들 인용회수가 각각 k 번 이하

# 1. k번 이상 인용된 논문이 k편 이상인지
# 2. k번 이하 인용된 논문이 n - k 편인지
for k in range(n+1):
    kup = 0
    kdown = 0
    for a in arr:
        if a >= k: kup += 1
        if a <= k: kdown += 1
    
    if kup >= k and kdown >= n - k:
        print(k)
        break