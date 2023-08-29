import sys
input = sys.stdin.readline
t = 1
while True:
    original = input().rstrip()
    source = input().rstrip()
    if original == 'END' and source == 'END': break

    if len(original) != len(source):
        print('Case %d: different'%t)
    else:
        original_dict = {chr(ord('a')+i):1 for i in range(26)}
        source_dict = {chr(ord('a')+i):1 for i in range(26)}
        for o in original: original_dict[o] += 1
        for s in source: source_dict[s] += 1

        if original_dict == source_dict:
            print('Case %d: same'%t)
        else:
            print('Case %d: different'%t)

    t += 1