import sys
input = sys.stdin.readline

while True:
    string = ""
    try:
        string = input().rstrip()
    except:
        break

    if string == "": break

    a, b = map(int, string.split())

    cnt = 0
    for i in range(a, b+1):
        done = 0
        for k in range(10):
            if str(i).count(str(k)) >= 2:
                done = 1
                break
        
        if done == 0: cnt += 1
    
    print(cnt)