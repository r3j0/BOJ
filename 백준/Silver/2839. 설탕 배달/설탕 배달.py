n = int(input())

startm3 = n//3
m3 = startm3
mim5s = 0
m5 = 0
min = n

for i in range(m3,-1,-1):
    mim5s = n - i*3
    if mim5s%5 == 0:
        m5 = mim5s//5
        if min > (i+m5):
            min = i+m5

if min == n:
    min = -1

print(min)