import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break

    arr = []
    for _ in range(n):
        name, height = input().rstrip().split()
        arr.append((name, float(height)))
    
    arr.sort(key=lambda x:-x[1])
    
    for na, he in arr:
        if he != arr[0][1]:
            break

        print(na, end=' ')
    print()