k,w,m = map(int, input().split())
if k>=w: print(0)
else: print((w-k)//m + (1 if (w-k)%m != 0 else 0))