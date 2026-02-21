a = input()

cnt = 0
string = "KOREA"
idx = 0
for i in range(len(a)):
    if (a[i] == string[idx]):
        cnt += 1
        idx = (idx + 1) % 5
print(cnt)