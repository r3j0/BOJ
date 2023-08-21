import sys
input = sys.stdin.readline

rsp = {'R':0, 'S':1, 'P':2}

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    player1_score = 0
    player2_score = 0
    for _ in range(n):
        a, b = input().rstrip().split()
        a = rsp[a]
        b = rsp[b]

        if a == b:
            pass
        elif (a < b and (not (a == 0 and b == 2))) or (a == 2 and b == 0):
            player1_score += 1
        else:
            player2_score += 1

    if player1_score == player2_score: print('TIE')
    elif player1_score > player2_score: print('Player 1')
    else: print('Player 2')

