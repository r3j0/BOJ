import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(n)]
dolrim = {
    '.':'.',
    'O':'O',
    '-':'|',
    '|':'-',
    '/':'\\',
    '\\':'/',
    '^':'<',
    '<':'v',
    'v':'>',
    '>':'^'
}

for j in range(m-1, -1, -1):
    for i in range(n):
        print(dolrim[arr[i][j]], end='')
    print()