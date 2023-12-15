def solution(s):
    answer = True
    
    op = 0
    for i in s:
        if i == '(': op += 1
        else: 
            if op == 0: return False
            op -= 1
    if op > 0: return False

    return True