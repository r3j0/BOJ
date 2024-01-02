import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
if b == 'miss': print(0)
elif b == 'bad': print(int(a)*200)
elif b == 'cool': print(int(a)*400)
elif b == 'great': print(int(a)*600)
elif b == 'perfect': print(int(a)*1000)