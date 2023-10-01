n, m = map(int, input().split())
print('NEWBIE!' if 1 <= m <= 2 else ('OLDBIE!' if m <= n else 'TLE!'))