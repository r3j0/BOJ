def solution(k, d):
    answer = 0
    a = 0
    while (a*k)**2 <= d**2:
        answer += int((((d**2) - ((a*k)**2))**(0.5)) // k) + 1
        a += 1
    return answer