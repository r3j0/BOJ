import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

a_dict = {}
b_dict = {}
for i in a:
    if a_dict.get(i): a_dict[i] += 1
    else: a_dict[i] = 1
for i in b:
    if b_dict.get(i): b_dict[i] += 1
    else: b_dict[i] = 1

res = []
for k, v in b_dict.items():
    if v != a_dict[k]: res.append(k)

print(''.join(res))