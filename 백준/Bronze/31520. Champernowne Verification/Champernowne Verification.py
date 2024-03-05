import sys
input = sys.stdin.readline

arr = int(input().rstrip())
answer = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910]
if arr in answer: print(answer.index(arr)+1)
else: print(-1)
