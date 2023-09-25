string = input().rstrip()
for s in string:
    print(s*(sum(list(map(int, list(str(ord(s))))))))