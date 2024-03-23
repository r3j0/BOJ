# 25379 : 피하자
# 홀수 or 짝수를 왼쪽 or 오른쪽으로 밉니다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
odd = 0
even = 0
odd_left_cost = 0
odd_right_cost = 0
even_left_cost = 0
even_right_cost = 0
for i in range(n):
    if arr[i] % 2 == 1:
        odd_left_cost += i - odd
        odd_right_cost += (n - 1 - i) - odd
    else:
        even_left_cost += i - even
        even_right_cost += (n - 1 - i) - even
    
    if arr[i] % 2 == 1: 
        odd += 1
    else: 
        even += 1
    
    #print(arr[i])
    #print(odd, even)
    #print(odd_left_cost, odd_right_cost, even_left_cost, even_right_cost)

print(min([odd_left_cost, odd_right_cost, even_left_cost, even_right_cost]))