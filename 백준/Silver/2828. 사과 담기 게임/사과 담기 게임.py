import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
j = int(input().rstrip())

left = 1
right = m
result = 0
for _ in range(j):
    tmp = int(input().rstrip())
    if left <= tmp <= right:
        continue
    else:
        if tmp < left:
            done = left - tmp
            result += done
            left -= done
            right -= done

        else: # right < tmp
            done = tmp - right
            result += done
            left += done
            right += done
print(result)