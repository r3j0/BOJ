import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    string = str(s).upper()
    if s == 'EOI': break

    if string.find('NEMO') != -1: print('Found')
    else: print('Missing')