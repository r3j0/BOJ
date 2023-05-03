def solution(string):
    stack = []
    num_string = ""
    back_par = 0

    for i in range(len(string)):
        #print(stack)
        ch = string[i]

        if ch in '1234567890':
            if back_par == 1: return "ROCK"
            num_string += ch        
        else:
            back_par = 0
            if (num_string == "" and ch != '(') or (num_string != "" and ch == '('):
                return "ROCK"
            
            if num_string != "":
                stack.append(int(num_string))
                num_string = ""

            if ch != ')':            
                stack.append(ch)
            else:
                back_par = 1
                if stack[-1] in ['+', '-', '*', '/', '(']:
                    return "ROCK"
                
                start_idx = len(stack) - 1
                while True:
                    if stack[start_idx] == '(':
                        break
                    if start_idx == 0:
                        return "ROCK"

                    start_idx -= 1
                
                idx = start_idx
                while True:
                    if len(stack) <= idx:
                        break

                    if stack[idx] in ['*', '/']:
                        if idx < len(stack) - 1 and idx > start_idx and stack[idx - 1] not in ['+', '-', '*', '/'] and stack[idx + 1] not in ['+', '-', '*', '/']:
                            res = 0
                            if stack[idx] == '*': res = stack[idx - 1] * stack[idx + 1]
                            elif stack[idx] == '/': res = stack[idx - 1] // stack[idx + 1]

                            for _ in range(2): del stack[idx - 1]
                            stack[idx - 1] = res
                            idx -= 1
                        else:
                            return "ROCK"
                    
                    idx += 1

                idx = start_idx
                while True:
                    if len(stack) <= idx:
                        break

                    if stack[idx] in ['+', '-']:
                        if idx < len(stack) - 1 and idx > start_idx and stack[idx - 1] not in ['+', '-'] and stack[idx + 1] not in ['+', '-']:
                            res = 0
                            if stack[idx] == '+': res = stack[idx - 1] + stack[idx + 1]
                            elif stack[idx] == '-': res = stack[idx - 1] - stack[idx + 1]

                            for _ in range(2): del stack[idx - 1]
                            stack[idx - 1] = res
                            idx -= 1
                        else:
                            return "ROCK"
                    
                    idx += 1
                
                result_ope = stack[-1]
                for _ in range(2): stack.pop()
                num_string = result_ope

    if num_string != "": stack.append(int(num_string))
    
    if '(' in stack: return "ROCK"

    idx = 0
    while True:
        #print(stack)
        if len(stack) <= idx:
            break

        if stack[idx] in ['*', '/']:
            if idx < len(stack) - 1 and idx > 0 and stack[idx - 1] not in ['+', '-', '*', '/'] and stack[idx + 1] not in ['+', '-', '*', '/']:
                res = 0
                if stack[idx] == '*': res = stack[idx - 1] * stack[idx + 1]
                elif stack[idx] == '/':
                    if stack[idx + 1] != 0:
                        res = stack[idx - 1] // stack[idx + 1]
                    else: return "ROCK"

                for _ in range(2): del stack[idx - 1]
                stack[idx - 1] = res
                idx -= 1
            else:
                return "ROCK"
        
        idx += 1

    idx = 0
    while True:
        #print(stack)
        if len(stack) == 1:
            break

        if stack[idx] in ['+', '-']:
            if idx < len(stack) - 1 and idx > 0 and stack[idx - 1] not in ['+', '-'] and stack[idx + 1] not in ['+', '-']:
                res = 0
                if stack[idx] == '+': res = stack[idx - 1] + stack[idx + 1]
                elif stack[idx] == '-': res = stack[idx - 1] - stack[idx + 1]

                for _ in range(2): del stack[idx - 1]
                stack[idx - 1] = res
                idx -= 1
            else:
                return "ROCK"
        
        idx += 1
    
    return stack[0]

string = input()
print(solution(string))