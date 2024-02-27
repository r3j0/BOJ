import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    c, v = map(int, input().rstrip().split())
    arr = []
    for _ in range(v):
        now_arr = list(map(int, input().rstrip().split()))
        arr.append(now_arr)
    
    vote = [0 for _ in range(c)]
    for i in range(v): vote[arr[i][0]-1] += 1
    if max(vote) >= v//2+1:
        print(vote.index(max(vote))+1, 1)
    else:
        first = 0
        second = 0
        if vote[first] < vote[1]:
            first = 1
            second = 0
        else:
            second = 1
        
        for i in range(2, c):
            if vote[second] < vote[i]:
                if vote[first] < vote[i]:
                    second = first
                    first = i
                else:
                    second = i
        
        vote_2 = [0 for _ in range(2)]
        for i in range(v):
            if arr[i].index(first+1) < arr[i].index(second+1):
                vote_2[0] += 1
            else:
                vote_2[1] += 1
        
        if vote_2[0] > vote_2[1]:
            print(first+1, 2)
        else:
            print(second+1, 2)
                    
