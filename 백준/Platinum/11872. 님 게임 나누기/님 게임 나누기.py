import sys      
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

result = 0

# 2e9
# *1 -> {*0} -> *1
# *2 -> {*0, *1, {*1|*1} -> *2
# *3 -> 3 -> *4
# *4 -> 0 1 2 4 1 3 -> 2 2 2 -> 0 -> 3
# *5 -> (1,4) 1 3 2 (2,3) 2 4 6 5
# *6 -> (1,5) 1 5 4 2 4 2 3 1 3 3 0 6
# *7 -> 16 7 25 7 3 4 7 8
# *8 -> 17 9 2 6 4 3 56 7
for a in arr:
    # 1. 돌 더미 하나 이상 제거
    # 2. 두 개의 비어있지 않은 돌 더미로 나누기
    now = a
    if a % 4 == 3: now += 1
    elif a % 4 == 0: now -= 1

    result ^= now
    

print('koosaga' if result != 0 else 'cubelover')