import sys
input = sys.stdin.readline

string = input().rstrip()
lis = []

for i in range(1, len(string)-1):
    one = string[:i]
    for j in range(i+1, len(string)):
        two = string[i:j]
        three = string[j:]
        lis.append(one[::-1] + two[::-1] + three[::-1])

lis.sort()
print(lis[0])