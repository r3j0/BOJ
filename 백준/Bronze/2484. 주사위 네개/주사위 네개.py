import sys
input = sys.stdin.readline

def gameScore(lis):
    if lis.count(lis[0]) == 4: 
        return 50000+lis[0]*5000
    elif lis.count(lis[0]) == 3 or lis.count(lis[1]) == 3:
        return 10000+lis[1]*1000
    elif lis[0] == lis[1] and lis[2] == lis[3]:
        return 2000+lis[0]*500+lis[2]*500
    elif lis[0] == lis[1] or lis[1] == lis[2]:
        return 1000+lis[1]*100
    elif lis[2] == lis[3]:
        return 1000+lis[2]*100
    else:
        return lis[3]*100

max_value = 0
n = int(input().rstrip())
for _ in range(n):
    arr = list(sorted(map(int, input().rstrip().split())))
    max_value = max(max_value, gameScore(arr))

print(max_value)