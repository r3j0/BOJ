import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = ' ' + input().rstrip() + ' '
    while True:
        arr = list(input().rstrip().split())
        if arr == ['what', 'does', 'the', 'fox', 'say?']:
            break
        
        while string.count(' ' + arr[2] + ' ') > 0:
            string = string.replace(' ' + arr[2] + ' ', ' ')
    
    print(string.strip())

