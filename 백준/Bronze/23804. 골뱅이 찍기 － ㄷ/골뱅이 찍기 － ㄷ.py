n = int(input())

def line():
    global n
    for _ in range(n): print('@@@@@'*n)

def vert():
    global n
    for _ in range(3):
        for _ in range(n):
            print('@'*n)

line()
vert()
line()