import sys
input = sys.stdin.readline

n = int(input())
stu = []
for _ in range(n):
    name, kor, eng, math = input().split()
    stu.append([name, int(kor), int(eng), int(math)])

stu.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in stu: print(i[0])