import datetime
a, b = map(int, input().rstrip().split())
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
result = days[datetime.date(2007, a, b).weekday()]
print(result)