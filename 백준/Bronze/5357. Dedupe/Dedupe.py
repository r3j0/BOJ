t=int(input())
for _ in range(t):
    string = input()
    now = string[0]
    print(string[0], end='')
    for i in range(1, len(string)):
        if now != string[i]:
            now = string[i]
            print(string[i], end='')
    print()