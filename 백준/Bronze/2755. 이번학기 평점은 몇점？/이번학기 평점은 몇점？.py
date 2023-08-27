import sys
input = sys.stdin.readline

n = int(input().rstrip())
score = 0
chong = 0
sungjukpyo = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}
for _ in range(n):
    name, hakjum, sungjuk = input().rstrip().split()
    score += sungjukpyo[sungjuk] * int(hakjum)
    chong += int(hakjum)

def roundUp(src):
    if '5' <= src[-1] <= '9':
        return ((float(src[:-1]) * 100) + 1) / 100
    else:
        return float(src[:-1])

print('%.2f'%(roundUp('%.3f'%(score/chong))))