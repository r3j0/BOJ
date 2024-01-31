import sys
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

result = -1

for d1 in range(1, 3*n):
    for d2 in range(1, 3*n):
        for x in range(1, n+1):
            if x + d1 + d2 > n: break
            for y in range(1, n+1):
                if not (1 <= y - d1 and y + d2 <= n): continue

                area = [[0 for _ in range(n)] for _ in range(n)]

                for d1i in range(d1 + 1): area[x - 1 + d1i][y - 1 - d1i] = 5
                for d2i in range(d2 + 1): area[x - 1 + d2i][y - 1 + d2i] = 5
                for d2i in range(d2 + 1): area[x - 1 + d1 + d2i][y - 1 - d1 + d2i] = 5
                for d1i in range(d1 + 1): area[x - 1 + d2 + d1i][y - 1 + d2 - d1i] = 5

                five_mode = 0
                for i in range(n):
                    for j in range(n):
                        if five_mode == 1: 
                            if area[i][j] == 5:
                                five_mode = 0
                            else:
                                area[i][j] = 5
                        else:
                            if area[i][j] == 5 and i != x - 1 and i != x - 1 + d1 + d2:
                                five_mode = 1
                            elif area[i][j] == 0:
                                if 1 <= i + 1 < x + d1 and 1 <= j + 1 <= y: area[i][j] = 1
                                elif 1 <= i + 1 <= x + d2 and y < j + 1 <= n: area[i][j] = 2
                                elif x + d1 <= i + 1 <= n and 1 <= j + 1 < y - d1 + d2: area[i][j] = 3
                                elif x + d2 < i + 1 <= n and y - d1 + d2 <= j + 1 <= n: area[i][j] = 4

                people = [0 for _ in range(5)]
                for i in range(n):
                    for j in range(n): 
                        people[area[i][j] - 1] += maps[i][j]
                
                """ if max(people) - min(people) == 18 or (x == 2 and y == 4 and d1 == 1 and d2 == 1):
                    print(x, y, d1, d2)
                    for i in range(n): print(' '.join(map(str, area[i])))
                    print() """

                if result == -1:
                    result = max(people) - min(people)
                else:
                    #print(result, max(people) - min(people))
                    result = min(result, max(people) - min(people))

print(result)