import sys
input = sys.stdin.readline

month, days, year, time = input().rstrip().split()
months_num = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = int(days[:-1])
hour, minute = map(int, time.split(':'))
year = int(year)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    months[1] += 1

now_days = minute + (hour * 60) + ((days - 1) * 24 * 60) + (sum([months[i-1] for i in range(1, months_num[month])]) * 24 * 60)

print(now_days / (sum(months) * 1440) * 100)