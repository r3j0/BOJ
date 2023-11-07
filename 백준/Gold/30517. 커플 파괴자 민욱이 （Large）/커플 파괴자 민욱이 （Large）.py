import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
lis = []
pre = 0
combs = 1
for i in range(1, n):
    if arr[i-1] == arr[i] != 0:
        lis.append([combs, arr[pre:i]])
        pre = i
        combs += 1

lis.append([combs, arr[pre:n]])

count = 0
exception_flag = False
result_arr = []
result_num = []
def backtracking(now_arr, now_num, left):
    global count
    global result_arr
    global result_num
    global exception_flag

    if len(left) == 0:
        count += 1
        result_arr.append(now_arr)
        result_num.append(now_num)
        return

    if len(now_arr) == 0 and len(left) == 2 and left[0][1][0] == left[1][1][-1] != 0:
        exception_flag = True
        # Left Div
        store_left = []
        for sss in left: store_left.append(sss)
        inLeft = []
        for lll in store_left: inLeft.append(lll)
        tmp = inLeft.pop()

        now = inLeft.pop()
        now_left = now[1]
        back_to_left = len(now_left)
        stack = []
        
        stack.append(now_left.pop())
        while len(now_left) != 0:
            inLeft = [[1, now_left], [2, stack[::-1]], [3, tmp[1]]]
            for l in range(len(inLeft)):
                if len(now_arr) == 0 or (not (now_arr[-1][-1] == inLeft[l][1][0] != 0)):
                    now_arr.append(list(inLeft[l][1]))
                    now_num.append(inLeft[l][0])
                    lltmp = inLeft[l]
                    del inLeft[l]

                    backtracking(list(now_arr), list(now_num), list(inLeft))
                    if count == 100: return
                    
                    back = inLeft[l:]
                    inLeft = inLeft[:l]
                    inLeft.append(lltmp)
                    inLeft.extend(back)
                    now_num.pop()
                    now_arr.pop()
            stack.append(now_left.pop())

        while len(now_left) != back_to_left:
            now_left.append(stack.pop())
        # Right Div
        inLeft = []
        for lll in store_left: inLeft.append(lll)
        now = inLeft.pop()

        tmp = inLeft.pop()
        now_left = now[1]
        stack = []
        
        stack.append(now_left[0])
        del now_left[0]
        while len(now_left) != 0:
            inLeft = [[1, tmp[1]], [2, stack], [3, now_left]]
            for l in range(len(inLeft)):
                if len(now_arr) == 0 or (not (now_arr[-1][-1] == inLeft[l][1][0] != 0)):
                    now_arr.append(list(inLeft[l][1]))
                    now_num.append(inLeft[l][0])
                    rrtmp = inLeft[l]
                    del inLeft[l]

                    backtracking(list(now_arr), list(now_num), list(inLeft))
                    if count == 100: return
                    
                    back = inLeft[l:]
                    inLeft = inLeft[:l]
                    inLeft.append(rrtmp)
                    inLeft.extend(back)
                    now_num.pop()
                    now_arr.pop()
            stack.append(now_left[0])
            del now_left[0]
    else:
        for l in range(len(left)):
            if len(now_arr) == 0 or (not (now_arr[-1][-1] == left[l][1][0] != 0)):
                now_arr.append(list(left[l][1]))
                now_num.append(left[l][0])
                tmp = left[l]
                del left[l]

                backtracking(list(now_arr), list(now_num), list(left))
                if count == 100: return
                
                back = left[l:]
                left = left[:l]
                left.append(tmp)
                left.extend(back)
                now_num.pop()
                now_arr.pop()
    
backtracking([], [], list(lis))
if count == 0:
    print(-1)
else:
    print(len(lis) + (1 if exception_flag else 0))
    for i in range(count):
        on = []
        for k in range(len(result_arr[i])):
            #print(result_arr[i][k], end=' ')
            for kk in range(len(result_arr[i])):
                if k + 1 == result_num[i][kk]:
                    on.append(result_arr[i][kk])
                    break
        #print()
        for ooo in on:
            #print(ooo, end=' ')
            print(len(ooo), end=' ')
        print()
        dic = {}
        for rn in range(len(result_num[i])):
            dic[result_num[i][rn]] = rn+1
        for rnn in range(len(result_num[i])):
            print(result_num[i][rnn], end=' ')
        print()
    if count != 100: print(-1)