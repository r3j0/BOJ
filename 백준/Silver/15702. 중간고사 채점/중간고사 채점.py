import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
score = list(map(int, input().rstrip().split()))
max_num = 999999
max_score = -1
for _ in range(m):
    arr = list(input().rstrip().split())
    num = int(arr[0])
    arr = arr[1:]

    now_score = 0
    for i in range(n):
        if arr[i] == 'O':
            now_score += score[i]
    
    if max_score < now_score:
        max_num = num
        max_score = now_score
    elif max_score == now_score and max_num > num:
        max_num = num

print(max_num, max_score)
