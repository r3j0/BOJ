import sys
input = sys.stdin.readline

n = int(input().rstrip())
on = {}
for _ in range(n):
    string = input().rstrip()

    if len(on) == 0: on[string] = 1
    else:
        now_string = string[1:] + string[:1]
        already = 0
        while now_string != string:
            if on.get(now_string):
                already = 1
                break
            now_string = now_string[1:] + now_string[:1]

        if already == 0:
            on[string] = 1

print(len(on))