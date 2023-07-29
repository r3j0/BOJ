import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    area, base = map(float, input().rstrip().split())
    print('The height of the triangle is %.2f units'%((area*2)/base))