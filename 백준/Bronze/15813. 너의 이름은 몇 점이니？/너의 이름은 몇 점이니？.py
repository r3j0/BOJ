n = int(input())
string = input()
res = 0
for s in string:
    res += ord(s) - ord('A') + 1
print(res)