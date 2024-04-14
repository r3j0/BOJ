import sys
input = sys.stdin.readline

n = int(input())

count = 1
sum = 1
start_index = 1
end_index = 1

while end_index != n:
    if sum > n: 
        sum -= start_index
        start_index += 1
    elif sum < n:
        end_index += 1
        sum += end_index
    else:
        end_index += 1
        sum += end_index
        count += 1

print(count)