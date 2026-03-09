# 14289 : 본대 산책 3
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
def_m = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    def_m[a-1][b-1] = 1
    def_m[b-1][a-1] = 1

d = int(input().rstrip())
MOD = 1000000007

def mul(dcnt):
    if dcnt == 1:
        return def_m
    tmp = mul(dcnt//2)
    tmp2 = list(tmp)
    tmp4 = [[0 for _ in range(n)] for _ in range(n)]

    if dcnt % 2 == 1:
        tmp3 = mul(1)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp4[i][j] = (tmp4[i][j] + (tmp2[i][k] * tmp3[k][j])) % MOD
    else:
        tmp4 = list(tmp2)
        
    tmp5 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp5[i][j] = (tmp5[i][j] + (tmp[i][k] * tmp4[k][j])) % MOD
    
    return tmp5
                    

matrix = mul(d)
print(matrix[0][0])