string = input().rstrip()
if string[0] == string[-1] == '"' and string[1:-1] != '': print(string[1:-1])
else: print('CE')