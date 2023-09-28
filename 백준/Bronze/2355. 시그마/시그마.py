a, b = map(int, input().split())
n1, n2 = min(a, b), max(a, b)
print(((n2*(n2+1))//2)-((n1*(n1-1))//2))