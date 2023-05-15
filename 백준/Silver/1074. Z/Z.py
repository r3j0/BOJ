import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)
n, r, c = map(int, input().split())

def fuc(rVal, cVal, startR, startC, endR, endC):
    counts = 0

    if (endR - startR == 0 and endC - startC == 0): return 0
    
    leftupStartR = startR
    leftupEndR = startR + (endR - startR) // 2
    leftdownStartR = startR + (endR - startR) // 2 + 1
    leftdownEndR = endR

    leftupStartC = startC
    leftupEndC = startC + (endC - startC) // 2
    rightupStartC = startC + (endC - startC) // 2 + 1
    rightupEndC = endC

    rightupStartR = startR
    rightupEndR = startR + (endR - startR) // 2
    rightdownStartR = startR + (endR - startR) // 2 + 1
    rightdownEndR = endR

    leftdownStartC = startC
    leftdownEndC = startC + (endC - startC) // 2
    rightdownStartC = startC + (endC - startC) // 2 + 1
    rightdownEndC = endC

    if(leftupStartR <= rVal <= leftupEndR and leftupStartC <= cVal <= leftupEndC):
        return counts + fuc(rVal, cVal, leftupStartR, leftupStartC, leftupEndR, leftupEndC)
    counts += (leftupEndR - leftupStartR + 1) ** 2
    
    if(rightupStartR <= rVal <= rightupEndR and rightupStartC <= cVal <= rightupEndC):
        return counts + fuc(rVal, cVal, rightupStartR, rightupStartC, rightupEndR, rightupEndC)
    counts += (rightupEndR - rightupStartR + 1) ** 2

    if(leftdownStartR <= rVal <= leftdownEndR and leftdownStartC <= cVal <= leftdownEndC):
        return counts + fuc(rVal, cVal, leftdownStartR, leftdownStartC, leftdownEndR, leftdownEndC)
    counts += (leftdownEndR - leftdownStartR + 1) ** 2
    
    return counts + fuc(rVal, cVal, rightdownStartR, rightdownStartC, rightdownEndR, rightdownEndC)
    


print(fuc(r, c, 0, 0, (2**n) - 1, (2**n) - 1))