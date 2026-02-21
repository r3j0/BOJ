n = int(input())
arr = list(map(int, input().split()))
ans = [0]
mins = arr[0]

for i in range(1, n):
    mins = min(mins, arr[i])
    ans.append(max(ans[-1], arr[i] - mins))

print(' '.join(map(str, ans)))