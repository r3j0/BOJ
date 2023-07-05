import sys
from math import *
input = sys.stdin.readline

def score(dista):
    if dista <= 3: return 100
    if dista <= 6: return 80
    if dista <= 9: return 60
    if dista <= 12: return 40
    if dista <= 15: return 20
    return 0

test = int(input().rstrip())
for _ in range(test):
    arr = list(map(float, input().rstrip().split()))
    first = 0
    for i in range(3):
        x, y = arr[i*2], arr[i*2+1]
        first += score(sqrt(x**2+y**2))
    
    second = 0
    for i in range(3, 6):
        x, y = arr[i*2], arr[i*2+1]
        second += score(sqrt(x**2+y**2))
    
    print("SCORE: %d to %d, %s"%(first, second, ('TIE.' if first == second else ('PLAYER 1 WINS.' if first > second else 'PLAYER 2 WINS.'))))