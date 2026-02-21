n, m = map(int, input().rstrip().split())

parent = [i for i in range(100001)]
def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: a, b = b, a
    parent[b] = a

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    union(a, b)

arr = list(map(int, input().rstrip().split()))
find(arr[0])
cnt = 0
for i in range(1, n):
    find(arr[i])
    if (parent[arr[i-1]] != parent[arr[i]]): cnt += 1
print(cnt)