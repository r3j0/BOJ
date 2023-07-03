import sys
input = sys.stdin.readline

maps = {
    'W':'Q', 'E':'W', 'R':'E', 'T':'R', 'Y':'T', 'U':'Y', 'I':'U', 'O':'I', 'P':'O', '[':'P', ']':'[', '\\':']',
    'S':'A', 'D':'S', 'F':'D', 'G':'F', 'H':'G', 'J':'H', 'K':'J', 'L':'K', ';':'L', "'":';',
    'X':'Z', 'C':'X', 'V':'C', 'B':'V', 'N':'B', 'M':'N', ',':'M', '.':',', '/':'.',
    '1':'`', '2':'1', '3':'2', '4':'3', '5':'4', '6':'5', '7':'6', '8':'7', '9':'8', '0':'9', '-':'0', '=':'-',
    ' ':' '
}

while True:
    string = ""
    try:
        string = input().rstrip()
    except:
        break

    if string == "": break

    for s in string:
        print(maps[s], end='')
    print()