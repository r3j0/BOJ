import sys
input = sys.stdin.readline

start_h, start_m, start_s = map(int, input().rstrip().split(':'))
end_h, end_m, end_s = map(int, input().rstrip().split(':'))

time = (end_h*3600+end_m*60+end_s) - (start_h*3600+start_m*60+start_s)
if time <= 0: time += (24*3600)
print('%02d:%02d:%02d'%(time//3600, (time%3600)//60, time%60))