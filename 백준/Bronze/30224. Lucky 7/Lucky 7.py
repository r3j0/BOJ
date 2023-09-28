"""
Print 0 if the number does not contain 7 and is not divisible by 7.
Print 1 if the number does not contain 7 but is divisible by 7.
Print 2 if the number does contain 7 but is not divisible by 7.
Print 3 if the number does contain 7 and is divisible by 7.
"""

n = int(input())

if str(n).count('7') > 0:
    if n % 7 == 0: print(3)
    else: print(2)
else:
    if n % 7 == 0: print(1)
    else: print(0)