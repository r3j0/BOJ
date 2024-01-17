import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# 1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16

# 9번째 수 찾기 : 6
# 10번째 수 찾기 : 6
# 11번째 수 찾기 : 8

# B[k] 보다 작은 수의 개수가 k 이상이 되어서는 안 됨
# B[k] 보다 작은 수의 개수는 k 미만

# 1 2 3 4 ( 6보다 작은 수 : 4개 ) ( 6보다 작거나 같은 수: 4개 )
# 2 4 6 8 ( 6보다 작은 수 : 2개 ) ( 6보다 작거나 같은 수: 3개 )
# 3 6 9 12 ( 6보다 작은 수 : 1개 ) ( 6보다 작거나 같은 수: 2개 )
# 4 8 12 16 ( 6보다 작은 수 : 1개 ) ( 6보다 작거나 같은 수: 1개 )

# 1 3 6 10 -> 6 선택. 2번째 행. 2번째 행의 마지막 수 : 6

def BinarySearch(start, end):
    global n
    global k
    if start == end: 
        print(start)
        return

    if start < end:
        mid = (start + end) // 2
        ons = 0
        for i in range(1, n+1): ons += min(mid // i, n)

        if ons < k: BinarySearch(mid + 1, end)
        else: BinarySearch(start, mid)

BinarySearch(1, n**2)