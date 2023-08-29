# 남규는 영훈이보다 2개 이상 많이
# 택희가 받는건 짝수

import sys
input = sys.stdin.readline

# 남 택 영
# 1 2 3

n = int(input().rstrip())
cnt = 0
for taek in range(1, n//2+1):
    if taek*2 >= n: break

    for nam in range(1, n-(taek*2)+1):
        for young in range(nam+2, n-(taek*2)-nam+1):
            if nam + young + taek * 2 == n:
                cnt += 1
print(cnt)