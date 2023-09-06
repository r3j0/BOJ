import sys 
input = sys.stdin.readline

n, x, y = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

"""
방문 순서를 만족하면서 할당량을 채우기 위해 제품 판매에 성공해야 하는 
최소 고객의 수를 출력한다. 이때 마지막으로 판매에 성공하는 고객의 번호를 
그 다음 줄에 출력하는데, 가능한 번호가 여러 개이면 그중 가장 작은 값을 출력한다.

어떠한 고객이 제품을 구입한다고 하더라도 할당량을 채울 수 없는 경우에는 
-1을 출력한다.

dp[person][i][j] : person 번한테까지 팔고 정확히 x 할당량 i y 할당량 j 팔았을 때 
                    판 최소 고객의 수
꼭 i j 까지 안팔아도 할당량은 초과할 수 있음.
dp[person][i][j] = dp[person - 1][i - now_x][j]
                   dp[person - 1][i][j - now_y]
                   dp[person - 1][i - now_x][j - now_y]
                   dp[person - 1][i][j]

i j 가 할당량 넘고 >0 이면 바로 출력
"""

dp = [[[51 for _ in range(201)] for _ in range(201)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 0

done = 0
dp_min = 51
dp_last_min = 51
for x_limit in range(1, 201):
    for y_limit in range(1, 201):
        for thing in range(1, n+1):
            now_x = arr[thing - 1][0]
            now_y = arr[thing - 1][1]

            tmp_dp = [dp[thing][x_limit][y_limit], dp[thing - 1][x_limit][y_limit]]
            if x_limit >= now_x and dp[thing - 1][x_limit - now_x][y_limit] != 51: 
                tmp_dp.append(dp[thing - 1][x_limit - now_x][y_limit] + 1)
            
            if y_limit >= now_y and dp[thing - 1][x_limit][y_limit - now_y] != 51:
                tmp_dp.append(dp[thing - 1][x_limit][y_limit - now_y] + 1)
                
            if x_limit >= now_x and y_limit >= now_y and dp[thing - 1][x_limit - now_x][y_limit - now_y] != 51:
                tmp_dp.append(dp[thing - 1][x_limit - now_x][y_limit - now_y] + 1)

            dp[thing][x_limit][y_limit] = min(tmp_dp)
            if x_limit >= x and y_limit >= y and (dp_min > dp[thing][x_limit][y_limit] or (dp_min == dp[thing][x_limit][y_limit] and dp_last_min > thing)):
                dp_last_min = thing
                dp_min = dp[thing][x_limit][y_limit]
        
        if x_limit >= x and y_limit >= y and dp_min != 51:
            done = 1

if done == 0: print(-1)
else:
    print(dp_min)
    print(dp_last_min)