import sys
input = sys.stdin.readline

string = list(map(int, list(input().rstrip())))
strOri = int(''.join(map(str, string)))
strLen = len(string)
strList = {}
for s in string:
    if strList.get(s): strList[s] += 1
    else: strList[s] = 1

answer = -1
def backtracking(now, cnt):
    global answer
    if cnt == strLen:
        nowList = {}
        for i in now:
            if nowList.get(i): nowList[i] += 1
            else: nowList[i] = 1
        
        if nowList == strList:
            go = int(''.join(map(str, now)))
            if go > strOri:
                if answer == -1: answer = go
                else: answer = min(answer, go)
        return

    for k in range(10):
        if k == 0 and cnt == 0: continue
        now.append(k)
        backtracking(now, cnt + 1)
        now.pop()

backtracking([], 0)
print(answer if answer != -1 else 0)
