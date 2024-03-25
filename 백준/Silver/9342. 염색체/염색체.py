import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    if len(string) > 0 and 'A' <= string[0] <= 'F':
        group = []
        now_alpha = string[0]
        now_cnt = 1
        for i in range(1, len(string)):
            if now_alpha == string[i]: now_cnt += 1
            else:
                group.append([now_alpha, now_cnt])
                now_alpha = string[i]
                now_cnt = 1
        group.append([now_alpha, now_cnt])

        if group[0][0] != 'A':
            if len(group) >= 4 and group[1][0] == 'A' and group[2][0] == 'F' and group[3][0] == 'C':
                if len(group) == 4 or (len(group) == 5 and 'A' <= group[4][0] <= 'F' and group[4][1] == 1): print('Infected!')
                else: print('Good')
            else: print('Good')
        else:
            if len(group) >= 3 and group[1][0] == 'F' and group[2][0] == 'C':
                if len(group) == 3 or (len(group) == 4 and 'A' <= group[3][0] <= 'F' and group[3][1] == 1): print('Infected!')
                else: print('Good')
            else: print('Good')
    else: print('Good')