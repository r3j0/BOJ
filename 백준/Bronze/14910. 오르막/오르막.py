import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))
print('Good' if sorted(arr) == arr else 'Bad')