string = str(input().rstrip())
print(len(string) + string.count(':') + (string.count('_') * 5))