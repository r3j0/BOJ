import sys
input = sys.stdin.readline

sh, sm, ss = map(int, input().rstrip().split(':'))
eh, em, es = map(int, input().rstrip().split(':'))
stime = ss + sm * 60 + sh * 3600
etime = es + em * 60 + eh * 3600

if stime >= etime: etime += 86400
time = etime - stime
print('%02d:%02d:%02d'%(time//3600, time%3600//60, time%60))