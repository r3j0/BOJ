import sys
input = sys.stdin.readline

w = float(input().rstrip())
h = float(input().rstrip())
r = w/(h*h)

if r > 25: print('Overweight')
elif 18.5 <= r <= 25: print('Normal weight')
else: print('Underweight')