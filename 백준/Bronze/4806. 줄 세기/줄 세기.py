import sys
input = sys.stdin.readline

cnt = 0
while True:
    string = ""
    try:
        string = input().rstrip()
    except:
        break

    if string == "": break
    cnt += 1
print(cnt)