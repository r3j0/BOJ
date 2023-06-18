import sys
input = sys.stdin.readline

lis = [
"baby", "sukhwan", "tururu", "turu",
"very", "cute", "tururu", "turu",
"in", "bed", "tururu", "turu",
"baby", "sukhwan"
]
n = int(input())
n -= 1

result = lis[n%14]
if result == "tururu" or result == "turu": 
    if (result == "tururu" and n // 14 >= 3): print("tu+ru*" + str(2+(n//14)))
    elif (result == "turu" and n // 14 >= 4): print("tu+ru*" + str(1+(n//14)))
    else: print(result + 'ru' * (n // 14))
else: print(result)