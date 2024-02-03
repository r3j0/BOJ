import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
now = n
while now != 1:
    for i in range(now//2):
        for j in range(now//2):
            max_value = -1
            max_s_value = -1
            for ki in range(2):
                for kj in range(2):
                    if max_value == -1: max_value = arr[i*2+ki][j*2+kj] 
                    elif max_s_value == -1:
                        if max_value < arr[i*2+ki][j*2+kj]:
                            max_s_value = max_value
                            max_value = arr[i*2+ki][j*2+kj]
                        else:
                            max_s_value = arr[i*2+ki][j*2+kj]
                    else:
                        if max_value < arr[i*2+ki][j*2+kj]:
                            max_s_value = max_value
                            max_value = arr[i*2+ki][j*2+kj] 
                        elif max_s_value < arr[i*2+ki][j*2+kj]:
                            max_s_value = arr[i*2+ki][j*2+kj]
            
            arr[i][j] = max_s_value
    
    now //= 2

print(arr[0][0])
