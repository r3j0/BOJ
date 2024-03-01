import sys
import heapq
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    min_queue = []
    min_queue_dic = {}
    max_queue = []
    max_queue_dic = {}

    def hpop(mode):
        if mode == 'min' and min_queue:
            min_queue_dic[min_queue[0]] -= 1
            if min_queue_dic[min_queue[0]] == 0:
                del min_queue_dic[min_queue[0]]
            heapq.heappop(min_queue)
        elif mode == 'max' and max_queue:
            max_queue_dic[-max_queue[0]] -= 1
            if max_queue_dic[-max_queue[0]] == 0:
                del max_queue_dic[-max_queue[0]]
            heapq.heappop(max_queue)

    for _ in range(n):
        order = list(input().rstrip().split())
        if order[0] == 'I':
            heapq.heappush(min_queue, int(order[1]))
            if min_queue_dic.get(int(order[1])): min_queue_dic[int(order[1])] += 1
            else: min_queue_dic[int(order[1])] = 1
            heapq.heappush(max_queue, -int(order[1]))
            if max_queue_dic.get(int(order[1])): max_queue_dic[int(order[1])] += 1
            else: max_queue_dic[int(order[1])] = 1
        else: #D
            if order[1] == '1': # 1 최댓값 지우기
                # 1. 안 지워진 값 지우기 (공통 큐로 만들기)
                while min_queue and max_queue and (not min_queue_dic.get(-max_queue[0]) or max_queue_dic[-max_queue[0]] > min_queue_dic[-max_queue[0]]):
                    hpop('max')
                if min_queue and max_queue and min_queue[0] == -max_queue[0]:
                    # 2. 공통된 값 지우기
                    hpop('min')
                    hpop('max')
                else:
                    # 3. 공통되지 않으면 먼저 지우기
                    if max_queue:
                        hpop('max')
            else: # -1 최솟값 지우기
                # 1. 안 지워진 값 지우기 (공통 큐로 만들기)
                while min_queue and max_queue and (not max_queue_dic.get(min_queue[0]) or min_queue_dic[min_queue[0]] > max_queue_dic[min_queue[0]]):
                    hpop('min')
                if min_queue and max_queue and min_queue[0] == -max_queue[0]:
                    # 2. 공통된 값 지우기
                    hpop('min')
                    hpop('max')
                else:
                    # 3. 공통되지 않으면 먼저 지우기
                    if min_queue:
                        hpop('min')
        """ print(min_queue)
        print(max_queue)
        print() """
    while min_queue and max_queue and (not min_queue_dic.get(-max_queue[0]) or max_queue_dic[-max_queue[0]] > min_queue_dic[-max_queue[0]]):
        hpop('max')
    while min_queue and max_queue and (not max_queue_dic.get(min_queue[0]) or min_queue_dic[min_queue[0]] > max_queue_dic[min_queue[0]]):
        hpop('min')
    if min_queue and max_queue:
        print(-max_queue[0], min_queue[0])
    else:
        print('EMPTY')