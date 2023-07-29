string = input()
idx = len(string) - 1
now = 0
result = 0
while idx >= 0:
    if now == 0:
        if string[idx] != '0':
            now = 1
    else:
        if string[idx] == '0':
            result += 1
    idx -= 1

print(result)