import sys
input = sys.stdin.readline

def findPosition(arr):
    point = [[arr[0], arr[1]], [arr[2], arr[3]], [arr[4], arr[5]], [arr[6], arr[7]]]

    p1 = []
    pc = []
    p2 = []
    ons = []
    for i in range(4):
        for j in range(i+1, 4):
            if point[i] == point[j]:
                pc = [point[i][0], point[i][1]]
                ons = [i, j]
                break

    for i in range(4):
        if p1 == [] and i not in ons:
            p1 = [point[i][0], point[i][1]]
            ons.append(i)
        if p1 != [] and p2 == [] and i not in ons:
            p2 = [point[i][0], point[i][1]]
    
    return p1, pc, p2

while True:
    arr = []
    try:
        arr = list(map(float, input().rstrip().split()))
    except:
        break
    if len(arr) == 0:
        break
    
    if arr[0] == arr[2] == arr[4] == arr[6] and arr[1] == arr[3] == arr[5] == arr[7]: # all same
        print('%.3f %.3f'%(arr[0], arr[1]))
    else:
        point1, point_center, point2 = findPosition(arr)
        print('%.3f %.3f'%(point1[0] + (point2[0]-point_center[0]), point1[1] + (point2[1]-point_center[1])))
