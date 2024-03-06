import sys
input = sys.stdin.readline

string = input().rstrip()
now_arr = ['1']
now_n = 1
for i in string:
    if i not in now_arr:
        now_n += 1
        while i not in list(str(now_n)): now_n += 1
        now_arr = list(str(now_n))
        
    now_arr = now_arr[now_arr.index(i)+1:]
    #print(now_arr, now_n)

print(now_n)