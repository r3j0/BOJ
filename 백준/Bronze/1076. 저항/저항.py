import sys
input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()
third = input().rstrip()

color = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 
         'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

print((color[first] * 10 + color[second]) * pow(10, color[third]))