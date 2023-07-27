import sys
input = sys.stdin.readline

t1, m1, t2, m2 = map(int, input().rstrip().split())
time1 = t1*60+m1
time2 = t2*60+m2

if time1 > time2: time2 += 24*60
print(time2-time1, (time2-time1)//30)