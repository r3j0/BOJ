import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    k = int(input().rstrip())
    arr = [input().rstrip() for _ in range(k)]

    string = ""
    for i in range(k):
        for j in range(k):
            if i == j: continue

            if arr[i] + arr[j] == str(arr[i] + arr[j])[::-1]:
                string = arr[i] + arr[j]
    
    if string == "": print(0)
    else: print(string)