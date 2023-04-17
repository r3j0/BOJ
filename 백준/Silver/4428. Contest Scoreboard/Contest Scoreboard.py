import sys
input = sys.stdin.readline
penalty = {}
score = {}
while True:
    try:
        team, problem, time, result = input().split()
        if penalty.get(team, -1) == -1:
            penalty[team] = {}
        
        if penalty[team].get(problem, -1) == -1:
            penalty[team][problem] = 0

        if score.get(team, -1) == -1:
            score[team] = {}
            
        if result == 'I':
            penalty[team][problem] += 1
        elif result == 'C':

            if score[team].get(problem, -1) == -1:
                score[team][problem] = penalty[team][problem] * 20 + int(time)
                penalty[team][problem] = 0
    
    except:
        break

last_standing = []
for s in score.keys():
    tmp = [s, len(score[s]), 0]
    for p in score[s].keys():
        tmp[2] += score[s][p]
    
    last_standing.append(tmp)

last_standing.sort(key=lambda x:(-x[1], -x[2], x[0]))
for l in last_standing:
    print(l[0], l[1], l[2])