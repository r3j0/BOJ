"""
[] _ _ _, _ _ _ []
_ [] _ _
_ _ [] _
"""

import sys
input = sys.stdin.readline

arr = list(sorted(map(int, input().rstrip().split())))

if arr[2] - arr[1] == arr[1] - arr[0]: print(arr[2] + arr[2] - arr[1])
elif arr[2] - arr[1] < arr[1] - arr[0]: print(arr[0] + arr[2] - arr[1])
else: print(arr[1] + arr[1] - arr[0])