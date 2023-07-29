string = input()
idx = 0
while idx < len(string):
    print(string[idx], end='')

    idx += ord(string[idx]) - ord('A') + 1