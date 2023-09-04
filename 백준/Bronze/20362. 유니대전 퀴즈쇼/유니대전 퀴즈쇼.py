import sys
input = sys.stdin.readline

n, s = input().rstrip().split()
answer_table = {}

already = 0
result = 0
result_answer = ""
for _ in range(int(n)):
    name, answer = input().rstrip().split()

    if name == s:
        already = 1
        result_answer = answer
    elif already == 0:
        if answer_table.get(answer): answer_table[answer] += 1
        else: answer_table[answer] = 1

if answer_table.get(result_answer): print(answer_table[result_answer])
else: print(0)