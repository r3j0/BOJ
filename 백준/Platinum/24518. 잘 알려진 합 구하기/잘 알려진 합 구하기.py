# 24518 : 잘 알려진 합 구하기
import sys 
input = sys.stdin.readline

MOD = 1_000_000_007

n, m = map(int, input().rstrip().split())

ans = 0
i = 1
j = 0
mod_i = i % m
while i <= n:
    j = n // (n // i)
    mod_j = j % m
    
    # 0 1 2 3
    # m이 4라면 구간길이//4마다 나머지*(나머지-1)//2 만큼 곱해짐
    # 3 0 1 2 / 3 0 1 2 / 3
    # 99 0 1 2 .. 98 / 99 0 1 2 3 4 
    
    k = mod_i
    if i != j:
        k = ((j-i+1)//m) * (m*(m-1)//2)
        if ((j-i+1)%m):
            if mod_i > mod_j:
                k += (m * (m - 1) // 2) - (mod_i * (mod_i - 1) // 2)
                mod_i = 0
            if mod_i <= mod_j:
                k += (mod_j * (mod_j + 1) // 2) - (mod_i * (mod_i - 1) // 2)

    ans = (ans + ((n // i) * k)) % MOD

    i = j + 1
    mod_i = i % m

print(ans)