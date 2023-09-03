alpha = {'aespa':'a',
'baekjoon':'b',
'cau':'c',
'debug':'d',
'edge':'e',
'firefox':'f',
'golang':'g',
'haegang':'h',
'iu':'i',
'java':'j',
'kotlin':'k',
'lol':'l',
'mips':'m',
'null':'n',
'os':'o',
'python':'p',
'query':'q',
'roka':'r',
'solvedac':'s',
'tod':'t',
'unix':'u',
'virus':'v',
'whale':'w',
'xcode':'x',
'yahoo':'y',
'zebra':'z'}

import sys
input = sys.stdin.readline

string = input().rstrip()
last = []
original = []
done = 0
for s in string:
    last.append(s)

    if alpha.get(''.join(last)):
        original.append(alpha[''.join(last)])
        last = []
    
    if len(last) > 8:
        done = 1
        break

if last == [] and done == 0:
    print('It\'s HG!')
    print(''.join(original))
else:
    print('ERROR!')