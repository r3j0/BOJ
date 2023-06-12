# Objects weighing 100.00 on Earth will weigh 16.70 on the moon.
import sys
input = sys.stdin.readline

while True:
    n = float(input().rstrip())
    if n < 0: break

    print('Objects weighing %.2f on Earth will weigh %.2f on the moon.'%(n, n*0.167))