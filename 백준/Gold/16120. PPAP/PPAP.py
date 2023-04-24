ppap = input()
stack = []

for i in range(len(ppap)):
    if ppap[i] == 'P':
        if len(stack) >= 3:
            if stack[-1] == 'A' and stack[-2] == 'P' and stack[-3] == 'P':
                for _ in range(3): stack.pop()
    stack.append(ppap[i])

#print(stack)
if len(stack) == 0: print("PPAP")
elif len(stack) == 1:
    if stack[0] == 'P': print("PPAP")
    else: print("NP")
else: print("NP")