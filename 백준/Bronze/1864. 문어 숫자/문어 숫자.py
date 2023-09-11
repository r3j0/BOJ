import sys
input = sys.stdin.readline

alpha = {
    '-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1
}

while True:
    string = input().rstrip()
    if string == '#': break

    now = 0
    for i in range(len(string)):
        now += alpha[string[i]] * (8**(len(string) - i - 1))
    
    print(now)