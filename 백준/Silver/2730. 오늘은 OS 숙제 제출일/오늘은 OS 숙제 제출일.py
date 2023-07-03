import sys
from datetime import datetime
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    aday, bday = input().rstrip().split()
    am, ad, ay = aday.split('/')
    bm, bd = bday.split('/')

    zam = am if len(am) == 2 else "0" + am
    zad = ad if len(ad) == 2 else "0" + ad
    zbm = bm if len(bm) == 2 else "0" + bm
    zbd = bd if len(bd) == 2 else "0" + bd

    now = datetime.strptime(ay+zam+zad, "%Y%m%d")
    done = 0

    try:
        comp1 = datetime.strptime(ay+zbm+zbd, "%Y%m%d")
        if abs((now-comp1).days) <= 7:
            done = 1
            if (now-comp1).days == 0: print('SAME DAY')
            elif (now-comp1).days < 0: print('%s/%s/%s IS %d DAY%s AFTER'%(bm, bd, ay, abs((now-comp1).days), ('S' if abs((now-comp1).days) > 1 else '')))
            elif (now-comp1).days > 0: print('%s/%s/%s IS %d DAY%s PRIOR'%(bm, bd, ay, abs((now-comp1).days), ('S' if abs((now-comp1).days) > 1 else '')))
    except:
        pass

    try:    
        comp2 = datetime.strptime(str(int(ay)-1)+zbm+zbd, "%Y%m%d")
        if abs((now-comp2).days) <= 7:
            done = 1
            if (now-comp2).days == 0: print('SAME DAY')
            elif (now-comp2).days < 0: print('%s/%s/%s IS %d DAY%s AFTER'%(bm, bd, str(int(ay)-1), abs((now-comp2).days), ('S' if abs((now-comp2).days) > 1 else '')))
            elif (now-comp2).days > 0: print('%s/%s/%s IS %d DAY%s PRIOR'%(bm, bd, str(int(ay)-1), abs((now-comp2).days), ('S' if abs((now-comp2).days) > 1 else '')))
    except:
        pass

    try:    
        comp3 = datetime.strptime(str(int(ay)+1)+zbm+zbd, "%Y%m%d")
        if abs((now-comp3).days) <= 7:
            done = 1
            if (now-comp3).days == 0: print('SAME DAY')
            elif (now-comp3).days < 0: print('%s/%s/%s IS %d DAY%s AFTER'%(bm, bd, str(int(ay)+1), abs((now-comp3).days), ('S' if abs((now-comp3).days) > 1 else '')))
            elif (now-comp3).days > 0: print('%s/%s/%s IS %d DAY%s PRIOR'%(bm, bd, str(int(ay)+1), abs((now-comp3).days), ('S' if abs((now-comp3).days) > 1 else '')))
    except:
        pass

    if done == 0:
        print('OUT OF RANGE')