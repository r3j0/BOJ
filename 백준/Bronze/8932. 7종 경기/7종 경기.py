import sys
input = sys.stdin.readline

t = int(input().rstrip())

def track(a, b, c, score):
    return int(a*((b-score)**c))
def field(a, b, c, score):
    return int(a*((score-b)**c))
a = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
b = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
c = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]
for _ in range(t):
    arr = list(map(int, input().rstrip().split()))

    result = 0
    for i in range(7):
        if i == 0 or i == 3 or i == 6: result += track(a[i], b[i], c[i], arr[i])
        else: result += field(a[i], b[i], c[i], arr[i])

    print(result)