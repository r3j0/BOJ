S = set()
arr = []
for _ in range(5):
    tmp = int(input())
    arr.append(tmp)
    S.add(tmp)
    
for i in S:
    if arr.count(i) % 2 == 1:
        print(i)
        break