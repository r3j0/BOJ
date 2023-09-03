import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
done = 0
for i in range(n - 4):
    now = string[i:i+5]
    if abs(ord(now[1]) - ord(now[0])) == 1 and abs(ord(now[2]) - ord(now[1])) == 1 and abs(ord(now[3]) - ord(now[2])) == 1 and abs(ord(now[4]) - ord(now[3])) == 1:
        done = 1
        break
print('YES' if done == 1 else 'NO')