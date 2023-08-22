import sys
input = sys.stdin.readline

aArr = list(map(int, input().rstrip().split()))
bArr = list(map(int, input().rstrip().split()))

a_score = 0
b_score = 0
drawing = 0
last_win = 0
for i in range(10):
    if aArr[i] > bArr[i]: 
        a_score += 3
        last_win = 1
    elif aArr[i] < bArr[i]: 
        b_score += 3
        last_win = 2
    else:
        drawing += 1
        a_score += 1
        b_score += 1

print(a_score, b_score)
if a_score == b_score: 
    if drawing == 10: print('D')
    else: print('A' if last_win == 1 else 'B')
else:
    if a_score > b_score: print('A')
    else: print('B')