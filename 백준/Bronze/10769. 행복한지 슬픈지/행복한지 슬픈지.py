import sys
input = sys.stdin.readline

string = input().rstrip()

happy_cnt = string.count(':-)')
sad_cnt = string.count(':-(')

if happy_cnt == 0 and sad_cnt == 0: print('none')
elif happy_cnt == sad_cnt: print('unsure')
elif happy_cnt > sad_cnt: print('happy')
else: print('sad')