import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

now_number = 0
now_str = ""
for s in string:
    if '0' <= s <= '9':
        now_str += s
    else:
        if now_str != "":
            now_number += int(now_str)
            now_str = ""

if now_str != "":
    now_number += int(now_str)

print(now_number)