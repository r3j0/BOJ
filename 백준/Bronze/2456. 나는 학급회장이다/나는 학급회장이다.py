import sys 
input = sys.stdin.readline

n = int(input().rstrip())

hubo = [{1:0, 2:0, 3:0} for _ in range(3)]
for _ in range(n):
    a, b, c = map(int, input().rstrip().split())
    hubo[0][a] += 1
    hubo[1][b] += 1
    hubo[2][c] += 1

hubo_score = []
for i in range(3):
    hubo_score.append(hubo[i][1] + hubo[i][2] * 2 + hubo[i][3] * 3)

if hubo_score.count(max(hubo_score)) == 1:
    print(hubo_score.index(max(hubo_score)) + 1, max(hubo_score))
else:
    # 3점 더 많이 받은 사람
    hubo_3count = []
    for i in range(3):
        if hubo_score[i] == max(hubo_score):
            hubo_3count.append(hubo[i][3])
        else:
            hubo_3count.append(0)
    
    if hubo_3count.count(max(hubo_3count)) == 1:
        print(hubo_3count.index(max(hubo_3count)) + 1, hubo_score[hubo_3count.index(max(hubo_3count))])
    else:
        # 2점 더 많이 받은 사람
        hubo_2count = []
        for i in range(3):
            if hubo_3count[i] == max(hubo_3count):
                hubo_2count.append(hubo[i][2])
            else:
                hubo_2count.append(0)

        if hubo_2count.count(max(hubo_2count)) == 1:
            print(hubo_2count.index(max(hubo_2count)) + 1, max(hubo_score))
        else:
            # 뭐야
            print(0, max(hubo_score))