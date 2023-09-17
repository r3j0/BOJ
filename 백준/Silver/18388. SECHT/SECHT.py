alpha = {
    'Q':'W', 'W':'E', 'E':'R', 'R':'T', 'T':'Y', 'Y':'U', 'U':'I', 'O':'P', 'P':'{',
    'A':'S', 'S':'D', 'D':'F', 'F':'G', 'G':'H', 'H':'J', 'J':'K', 'K':'L', 'L':':',
    'Z':'X', 'X':'C', 'C':'V', 'V':'B', 'B':'N', 'N':'M', 'M':'<'
}

import sys
input = sys.stdin.readline

string = input().rstrip()
for s in string:
    if 'A' <= s <= 'Z':
        print(alpha[s], end='')
    else:
        print(s,end='')