import sys
input = sys.stdin.readline

string = input().rstrip()
if string.count(string[0]) == len(string): print(-1)
else:
    # 앞뒤 글자가 다르면 팰린드롬
    # AAACAAAA 같은건 어케 판단하지?
    s = list(string)
    if s != s[::-1]: print(len(string))
    else: print(len(string)-1)