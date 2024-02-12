import sys
input = sys.stdin.readline

string = input().rstrip()
arr = [[] for _ in range(26)]
for i in range(52):
    arr[ord(string[i])-ord('A')].append(i)

res = 0
for i in range(25):
    for j in range(i+1, 26):
        if (arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] and arr[j][0] < arr[i][1]) or (arr[j][0] < arr[i][0] and arr[j][1] < arr[i][1] and arr[i][0] < arr[j][1]): res += 1

print(res)