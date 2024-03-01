import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(input().rstrip().split())
    dic = {}
    for a in arr:
        if dic.get(a): dic[a] += 1
        else: dic[a] = 1
    
    done = False
    # 3 이상 찾기
    for k, v in list(dic.items()):
        if v >= 3:
            done = True
            print(0)
            break
        
    if done == False:
        res = -1
        # 2-1 찾기
        for k, v in list(dic.items()):
            if v == 2:
                for kk, vv in list(dic.items()):
                    if v <= 2 and k != kk:
                        cnt = 0
                        for i in range(4):
                            if k[i] != kk[i]: cnt += 1
                        cnt *= 2
                        if res == -1 or res > cnt: res = cnt
        # 1 3개 찾기
        for k, v in list(dic.items()):
            for kk, vv in list(dic.items()):
                for kkk, vvv in list(dic.items()):
                    if k != kk and kk != kkk and k != kkk and v == 1 and vv == 1 and vvv == 1:
                        cnt = 0
                        for i in range(4):
                            if k[i] != kk[i]: cnt += 1
                        for i in range(4):
                            if kk[i] != kkk[i]: cnt += 1
                        for i in range(4):
                            if k[i] != kkk[i]: cnt += 1
                        if res == -1 or res > cnt: res = cnt
        print(res)