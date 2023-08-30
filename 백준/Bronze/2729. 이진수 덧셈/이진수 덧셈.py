import sys
input = sys.stdin.readline 

t = int(input().rstrip())
for _ in range(t):
    a, b = input().rstrip().split()
    print(str(bin(int('0b'+a, 2) + int('0b'+b, 2)))[2:])