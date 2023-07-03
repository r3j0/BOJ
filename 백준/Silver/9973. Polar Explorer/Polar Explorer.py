import sys
input = sys.stdin.readline

while True:
    start = input().rstrip()
    if start == "ENDOFINPUT": break

    x, y, z = map(int, input().rstrip().split())
    end = input().rstrip()

    dist = 2*x*3.14159 * (min(z, 360-z)/360) *2
    avail = y * 5
    #print(dist)
    #print(avail)
    if dist > avail:
        print('NO %d'%(avail))
    else:
        print('YES %d'%((avail-dist)//5))