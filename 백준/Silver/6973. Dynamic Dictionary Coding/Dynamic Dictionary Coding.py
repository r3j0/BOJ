import sys
input = sys.stdin.readline

test = int(input().rstrip())
for i in range(test):
    if i != 0: print()
    strs = []
    while True:
        string = input().rstrip()
        if string == "": break
        strs.append(string)
    
    dic = {}
    for s in strs:
        arr = list(s.split())
        for a in range(len(arr)):
            if a != 0: print(' ', end='')
            if dic.get(arr[a]): print(dic[arr[a]], end='')
            else: 
                dic[arr[a]] = len(dic) + 1
                print(arr[a], end='')
        print()