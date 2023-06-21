a, b = map(int, input().rstrip().split())
if a*7 == b*13:
    print('lika')
elif a*7 > b*13:
    print('Axel')
else:
    print('Petra')