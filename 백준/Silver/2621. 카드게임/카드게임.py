import sys
input = sys.stdin.readline

arr = [list(input().rstrip().split()) for _ in range(5)]
for i in range(5): arr[i][1] = int(arr[i][1])

col_count = {}
num_count = {}
for i in range(5):
    if col_count.get(arr[i][0]): col_count[arr[i][0]] += 1
    else: col_count[arr[i][0]] = 1
    if num_count.get(arr[i][1]): num_count[arr[i][1]] += 1
    else: num_count[arr[i][1]] = 1
# 1
if max(list(num_count.keys())) - min(list(num_count.keys())) == 4 and len(col_count) == 1:
    print(900+max(list(num_count.keys())))
# 2
elif len(num_count) == 2 and list(sorted(list(num_count.values()))) == [1, 4]:
    now = list(num_count.items())
    if now[0][1] == 4: print(800 + now[0][0])
    else: print(800 + now[1][0])
# 3
elif len(num_count) == 2 and list(sorted(list(num_count.values()))) == [2, 3]:
    now = list(num_count.items())
    if now[0][1] == 2: print(700 + now[1][0]*10 + now[0][0])
    else: print(700 + now[0][0]*10 + now[1][0])
# 4
elif len(col_count) == 1:
    print(600 + max(list(num_count.keys())))
# 5
elif len(num_count) == 5 and max(list(num_count.keys())) - min(list(num_count.keys())) == 4:
    print(500 + max(list(num_count.keys())))
# 6
elif 3 in list(num_count.values()):
    for k, v in list(num_count.items()):
        if v == 3:
            print(400 + k)
            break
# 7
elif len(num_count) == 3 and list(sorted(list(num_count.values()))) == [1, 2, 2]:
    arr = []
    for k, v in list(num_count.items()):
        if v == 2:
            arr.append(k)
    print(300 + max(arr)*10 + min(arr))
# 8
elif 2 in list(num_count.values()):
    for k, v in list(num_count.items()):
        if v == 2:
            print(200 + k)
            break
# 9
else:
    print(100 + max(list(num_count.keys())))


