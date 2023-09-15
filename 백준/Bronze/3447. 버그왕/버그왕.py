import sys
input = sys.stdin.readline

blank_cnt = 0
while True:
    string = input().rstrip()
    if string == "":
        blank_cnt += 1
        if blank_cnt > 1000: break
        continue
    else:
        for _ in range(blank_cnt): print()
        blank_cnt = 0
    
    while string.find('BUG') != -1:
        string = string.replace('BUG', '')
    
    print(string)