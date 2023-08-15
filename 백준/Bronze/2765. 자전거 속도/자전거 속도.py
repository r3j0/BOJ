import sys
import math
input = sys.stdin.readline

now = 1
while True:
    a, b, c = map(float, input().rstrip().split())
    if b == 0: break
        
    dist = a*b*math.pi*25.4*6.21371e-7
    print('Trip #%d: %.2f %.2f'%(now, dist, dist/(c/3600)))
    now += 1