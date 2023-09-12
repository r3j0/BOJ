import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
a, b = map(int, input().split())
print(days[datetime.date(2009, b, a).weekday()])
