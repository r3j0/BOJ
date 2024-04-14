import sys
input = sys.stdin.readline

s, p = map(int, input().rstrip().split())
string = input().rstrip()
order = list(map(int, input().rstrip().split()))

now = {'A':0, 'C':0, 'G':0, 'T':0}
for i in range(p): now[string[i]] += 1

result = 0
if now['A'] >= order[0] and now['C'] >= order[1] and now['G'] >= order[2] and now['T'] >= order[3]: result += 1 

for i in range(p, s):
    now[string[i]] += 1
    now[string[i-p]] -= 1

    if now['A'] >= order[0] and now['C'] >= order[1] and now['G'] >= order[2] and now['T'] >= order[3]: result += 1 

print(result)