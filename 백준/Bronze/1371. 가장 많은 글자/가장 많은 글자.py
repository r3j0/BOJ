import sys
input = sys.stdin.readline

arr = [0 for _ in range(26)]
endline_cnt = 0
while True:
    try:
        string = input().rstrip()
    except:
        break
    if string == "": 
        endline_cnt += 1
        if endline_cnt >= 100: break
        continue

    for s in string:
        if 'a' <= s <= 'z':
            arr[ord(s) - ord('a')] += 1

for i in range(26):
    if arr[i] == max(arr) and arr[i] != 0: print(chr(i + ord('a')), end='')