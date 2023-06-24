n = int(input())
lis = sorted(list(map(int,input().split())))

# 한 숫자가 리스트 안에 몇 개 있는지 딕셔너리로 저장
dic = {}
for i in lis:
    if dic.get(i): dic[i] += 1
    else: dic[i] = 1
key_list = list(dic.keys())

# 1개일 시 출력, 2개일 시 연속 여부 확인하고 출력
if len(key_list) == 1: print(' '.join(map(str, lis)))
elif len(key_list) == 2:
    if key_list[1] - key_list[0] == 1:
        for _ in range(dic[key_list[1]]): print(key_list[1], end=' ')
        for _ in range(dic[key_list[0]]): print(key_list[0], end=' ')
    else:
        for _ in range(dic[key_list[0]]): print(key_list[0], end=' ')
        for _ in range(dic[key_list[1]]): print(key_list[1], end=' ')
else:
    last_print = 0 # 가장 최근에 출력한 수
    printed = 0
    while True:
        # 남은 키가 2개면, 연속 여부 확인하고 연속이 아니면 계속 진행
        # 남은 키가 1개면, 전체 출력 후 종료. 남은 키가 없으면 종료.
        if len(key_list) == 2 and key_list[1] - key_list[0] == 1:
            for _ in range(dic[key_list[1]]): print(key_list[1], end=' ')
            for _ in range(dic[key_list[0]]): print(key_list[0], end=' ')
            break
        elif len(key_list) == 1:
            for _ in range(dic[key_list[0]]): print(key_list[0], end=' ')
            break
        elif len(key_list) == 0: break
        else:
            if printed == 0: # 처음 출력 ( 숫자 전체 다 출력 )
                for _ in range(dic[key_list[0]]): print(key_list[0], end=' ')
                last_print = key_list[0]
                del key_list[0]
                printed = 1
            else:
                # 숫자 1개씩만 출력하기 ( 더 나은 사전순이 있을 수 있음 )
                if key_list[0] - last_print == 1: # 이전에 출력했던 거랑 연속일 때 건너뛰기
                    print(key_list[1], end=' ')
                    last_print = key_list[1]

                    dic[key_list[1]] -= 1
                    if dic[key_list[1]] == 0: del key_list[1]
                else:
                    for _ in range(dic[key_list[0]]): print(key_list[0], end=' ')
                    last_print = key_list[0]

                    del key_list[0]