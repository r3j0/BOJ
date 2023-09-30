import sys
input = sys.stdin.readline

scores = list(map(int, input().split()))
my_score = int(input().rstrip())
scores.sort(reverse=True)
now = scores.index(my_score) + 1
if now <= 5: print('A+')
elif now <= 15: print('A0')
elif now <= 30: print('B+')
elif now <= 35: print('B0')
elif now <= 45: print('C+')
elif now <= 48: print('C0')
else: print('F')