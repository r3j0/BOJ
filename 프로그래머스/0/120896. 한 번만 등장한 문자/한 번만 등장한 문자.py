def solution(s):
    answer = ''
    dic = {}
    for i in s:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    res = []
    for k, v in list(dic.items()):
        if v == 1: res.append(k)
    res.sort()
    answer = ''.join(res)
    
    return answer