import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

# 투 포인터
start = 0
end = 1
result = 0
num_dict = {i:0 for i in range(100001)}
num_dict[arr[0]] = 1
while True:
    while end < n and num_dict[arr[end]] == 0:
        num_dict[arr[end]] = 1
        end += 1
    
    if start == end: break
    
    result += end - start
    num_dict[arr[start]] -= 1
    start += 1

print(result)