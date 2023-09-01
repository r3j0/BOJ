import sys
input = sys.stdin.readline

def twl(num):
    string = ""
    now = num
    while num >= 1:
        now = num % 12
        if now >= 10: 
            now = chr(ord('a') + (now - 10))
        string += str(now)

        num //= 12
    if num != 0: string += str(num)
    return string[::-1]

def otherSum(l):
    sums = 0
    for i in l:
        if '0' <= i <= '9': sums += int(i)
        else: sums += ord(i) - ord('a') + 10
    return sums


for i in range(1000, 10000):
    a = sum(list(map(int, list(str(i)))))
    b = otherSum(list(twl(i)))
    c = otherSum(list(str(hex(i))[2:]))

    if a == b == c: print(i)