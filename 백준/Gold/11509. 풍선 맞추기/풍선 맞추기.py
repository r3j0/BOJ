import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arrow = {}
for i in range(n):
    if len(arrow) == 0:
        arrow[arr[i]-1] = 1
    else:
        if arrow.get(arr[i], -1) != -1:
            arrow[arr[i]] -= 1
            if arrow[arr[i]] == 0:
                del arrow[arr[i]]
            
            if arrow.get(arr[i]-1, -1) == -1:
                arrow[arr[i]-1] = 1
            else:
                arrow[arr[i]-1] += 1
        else:
            if arrow.get(arr[i]-1, -1) == -1:
                arrow[arr[i]-1] = 1
            else:
                arrow[arr[i]-1] += 1
    #print(arrow)
print(sum(list(arrow.values())))