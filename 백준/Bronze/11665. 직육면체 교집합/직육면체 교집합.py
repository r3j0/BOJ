n = int(input())
min_x = 1000
min_y = 1000
min_z = 1000
max_x = 1
max_y = 1
max_z = 1
for _ in range(n):
    x1, y1, z1, x2, y2, z2 = map(int, input().rstrip().split())
    max_x = max(max_x, x1)
    max_y = max(max_y, y1)
    max_z = max(max_z, z1)
    min_x = min(min_x, x2)
    min_y = min(min_y, y2)
    min_z = min(min_z, z2)

res = 0
if min_x > max_x and min_y > max_y and min_z > max_z: 
    res = (min_x-max_x)*(min_y-max_y)*(min_z-max_z)
print(max(res, 0))