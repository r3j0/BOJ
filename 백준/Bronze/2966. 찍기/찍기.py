import sys
input = sys.stdin.readline

sanggeun = "ABC"
changyoung = "BABC"
hyunjin = "CCAABB"

s_idx = 0
c_idx = 0
h_idx = 0

s_res = 0
c_res = 0
h_res = 0

n = int(input().rstrip())
string = input().rstrip()

for s in string:
    if s == sanggeun[s_idx]:
        s_res += 1
    s_idx = (s_idx + 1) % len(sanggeun)
    if s == changyoung[c_idx]:
        c_res += 1
    c_idx = (c_idx + 1) % len(changyoung)
    if s == hyunjin[h_idx]:
        h_res += 1
    h_idx = (h_idx + 1) % len(hyunjin)
arr = []
arr.append((s_res, 'Adrian'))
arr.append((c_res, 'Bruno'))
arr.append((h_res, 'Goran'))

arr.sort(key=lambda x:(-x[0], x[1]))
max_value = max([s_res, c_res, h_res])

print(max_value)
for ar, an in arr:
    if ar == max_value:
        print(an)