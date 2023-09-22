n = int(input())
scores = list(map(int, input().split()))
maxs = max(scores)
print(sum(scores) / maxs * 100 / len(scores))