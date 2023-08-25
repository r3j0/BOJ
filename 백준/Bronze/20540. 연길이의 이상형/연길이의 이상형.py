import sys
input = sys.stdin.readline

mbti = {
    'E':'I', 'I':'E',
    'S':'N', 'N':'S',
    'T':'F', 'F':'T',
    'J':'P', 'P':'J'
}
string = input().rstrip()
for s in string:
    print(mbti[s], end='')