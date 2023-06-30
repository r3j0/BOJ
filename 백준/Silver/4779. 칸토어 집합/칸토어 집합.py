import sys
input = sys.stdin.readline

def blank(k):
    print(' '*k, end='')

def canto(k):
    if k == 1:
        print('-', end='')
    else:
        canto(k//3)
        blank(k//3)
        canto(k//3)
    

while True:
    try:
        n = int(input())
        canto(3**n)
        print()
    except:
        break