import sys
import math
input = sys.stdin.readline

d, h, w = map(int, input().split())
print(int(math.floor(math.sqrt(((d**2)*(h**2))/((w**2)+(h**2))))), int(math.floor(math.sqrt(((d**2)*(h**2))/((w**2)+(h**2)))*w/h)))