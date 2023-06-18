import sys
input = sys.stdin.readline

while True:
    string = list(input().rstrip())
    if string == ['0']: break
    
    count1 = string.count('1')
    count0 = string.count('0')
    counts = len(string) - count1 - count0

    print(len(string) + 1 + (count1 * 2) + (count0 * 4) + (counts * 3))

