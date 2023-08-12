string = input().rstrip().upper()
arr = []
for i in range(26): arr.append([chr(ord('A') + i), string.count(chr(ord('A') + i))])
arr.sort(key=lambda x:-x[1])

if arr[0][1] == arr[1][1]: print('?')
else: print(arr[0][0])