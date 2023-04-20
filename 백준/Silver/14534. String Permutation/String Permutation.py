def backtracking(string, result, dict):
    if len(string) == len(result):
        print(result)
        return
    
    for s in range(len(string)):
        if dict.get(s, -1) == -1:
            dict[s] = 1
            backtracking(string, result + string[s], dict)
            del dict[s]

test = int(input())
for t in range(test):
    string = input()
    print('Case # %d:'%(t+1))

    backtracking(string, "", {})
