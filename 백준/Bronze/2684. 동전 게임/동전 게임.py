import sys
input = sys.stdin.readline

test = int(input().rstrip())
for t in range(test):
    string = str(input().rstrip())
    result = [0 for _ in range(8)]
    now = string[:3]
    nowidx = 3
    while True:
        if now == 'TTT': result[0] += 1
        elif now == 'TTH': result[1] += 1
        elif now == 'THT': result[2] += 1
        elif now == 'THH': result[3] += 1
        elif now == 'HTT': result[4] += 1
        elif now == 'HTH': result[5] += 1
        elif now == 'HHT': result[6] += 1
        elif now == 'HHH': result[7] += 1
        if nowidx == 40: break
        now = now[1:] + string[nowidx]
        nowidx += 1
    
    print(' '.join(map(str, result)))