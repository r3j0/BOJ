import sys
input = sys.stdin.readline

for _ in range(3):
    string = input().rstrip()
    now_number = 0
    now_cnt = 0
    max_cnt = 0

    for i in range(8):
        if i == 0: 
            now_number = string[i]
            now_cnt += 1
        else:
            if now_number == string[i]: now_cnt += 1
            else: 
                now_number = string[i]
                now_cnt = 1
        
        max_cnt = max(max_cnt, now_cnt)
    print(max_cnt)