import sys
input = sys.stdin.readline

n = int(input().rstrip())
words = [[list(input().rstrip()), i] for i in range(n)]

words.sort(key=lambda x:(x[0], x[1]))
max_cnt = -1
max_num = [-1, -1]
max_idx = [-1, -1]
for i in range(n-1):
    for j in range(i+1, n):
        cnt = 0
        while len(words[i][0]) > cnt and len(words[j][0]) > cnt and words[i][0][cnt] == words[j][0][cnt]: cnt += 1
        #print(''.join(words[i][0]), ''.join(words[i+1][0]), cnt)
        if cnt == 0: break
        if max_cnt < cnt:
            max_cnt = cnt
            max_num = [words[i][1], words[j][1]]
            max_idx = [i, j]
        elif max_cnt == cnt:
            if min(max_num) > min(words[i][1], words[j][1]):
                max_num = [words[i][1], words[j][1]]
                max_idx = [i, j]
            elif min(max_num) == min(words[i][1], words[j][1]) and max(max_num) > max(words[i][1], words[j][1]):
                max_num = [words[i][1], words[j][1]]
                max_idx = [i, j]

if max_num[0] < max_num[1]: 
    print(''.join(words[max_idx[0]][0]))
    print(''.join(words[max_idx[1]][0]))
else:
    print(''.join(words[max_idx[1]][0]))
    print(''.join(words[max_idx[0]][0]))