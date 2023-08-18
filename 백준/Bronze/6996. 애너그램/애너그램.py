import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = input().rstrip().split()
    print('%s & %s are '%(a, b) + ('' if list(sorted(list(a))) == list(sorted(list(b))) else 'NOT ') + 'anagrams.')