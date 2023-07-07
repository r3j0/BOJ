t = int(input())
for _ in range(t):
    string = input()
    
    cnt = 0
    for i in range(len(string)):
        if string[i] == 'D':
            break
        cnt += 1
    print(cnt)
    