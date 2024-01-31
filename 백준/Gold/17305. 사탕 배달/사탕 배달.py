import sys
input = sys.stdin.readline

n, w = map(int, input().rstrip().split())
candy3 = []
candy5 = []

for _ in range(n):
    t, s = map(int, input().rstrip().split())
    if t == 3: candy3.append(s)
    else: candy5.append(s)

candy3.sort(reverse=True)
candy5.sort(reverse=True)

candy3_sum = [0]
candy5_sum = [0]

for i in candy3: candy3_sum.append(candy3_sum[-1] + i)
for i in candy5: candy5_sum.append(candy5_sum[-1] + i)

# 일단 먼저 5개를 다 넣어 놓고. ( 부족한 건 3개로 채우고 )
# 5개 사탕을 1개씩 빼면서 3개 계속 채우면서 확인하기

max_result = 0
last_w = w
result = 0

now_candy5 = min(len(candy5), last_w // 5)
result += candy5_sum[now_candy5]
last_w -= now_candy5 * 5

now_candy3 = min(len(candy3), last_w // 3)
result += candy3_sum[now_candy3]
last_w -= now_candy3 * 3

max_result = result
#print(now_candy5, now_candy3, result)

size = now_candy5
for i in range(size):
    result -= candy5[now_candy5 - 1]
    now_candy5 -= 1
    last_w += 5

    #print('last', len(candy3) - now_candy3)
    go_candy3 = min(len(candy3) - now_candy3, last_w // 3)
    result += candy3_sum[now_candy3 + go_candy3] - candy3_sum[now_candy3]
    last_w -= go_candy3 * 3
    now_candy3 += go_candy3
    
    max_result = max(max_result, result)
    #print(now_candy5, now_candy3, result)

print(max_result)