a = int(input())
b = int(input())
print(a*b - (((a-2)*(b-2)) if a-2>0 and b-2>0 else 0))