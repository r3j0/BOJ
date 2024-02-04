def solution(rsp):
    wins = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    for i in rsp: answer += wins[i]
    return answer