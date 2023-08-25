import sys
input = sys.stdin.readline

arr = []
space_cnt = 0
while True:
    try:
        now = input().rstrip()
    except:
        break

    if now == '': 
        space_cnt += 1 
        if space_cnt >= 100:
            break
    else:
        space_cnt = 0
        arr.extend(list(now.split()))

arr = arr[1:]
new_arr = []

for a in arr:
    new_arr.append(int(''.join(reversed(list(a)))))

new_arr.sort()
for a in new_arr:
    print(a)