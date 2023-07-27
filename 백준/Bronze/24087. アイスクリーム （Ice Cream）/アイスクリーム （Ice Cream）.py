s = int(input())
a = int(input())
b = int(input())

if s <= a: print(250)
else:
    now = a
    nowmoney = 250
    while s > now:
        now += b
        nowmoney += 100
    
    print(nowmoney)