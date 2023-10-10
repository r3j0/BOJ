import sys
input = sys.stdin.readline

year, month, day = map(int, input().rstrip().split('-'))
if year < 2023 or (year == 2023 and month < 9) or (year == 2023 and month == 9 and day <= 16): print("GOOD")
else: print("TOO LATE")