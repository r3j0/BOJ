import sys
input = sys.stdin.readline

string = input().rstrip()

for i in range(5):
    for j in range(len(string)):
        if i == 0 or i == 4:
            print('..#.' if (j + 1) % 3 != 0 else '..*.',end='')
            if j == len(string) - 1:
                print('.')
        elif i == 1 or i == 3:
            print('.#.#' if (j + 1) % 3 != 0 else '.*.*',end='')
            if j == len(string) - 1:
                print('.')
        elif i == 2:
            print('%c.%c.'%(('*' if j > 0 and j % 3 == 0 else '#'), string[j]) if (j + 1) % 3 != 0 else '*.%c.'%(string[j]), end='')
            if j == len(string) - 1:
                print('#' if (j + 1) % 3 != 0 else '*')