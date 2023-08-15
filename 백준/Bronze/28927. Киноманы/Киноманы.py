import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
print('Max' if a*3+b*20+c*120 > d*3+e*20+f*120 else ('Mel' if a*3+b*20+c*120 < d*3+e*20+f*120 else 'Draw'))