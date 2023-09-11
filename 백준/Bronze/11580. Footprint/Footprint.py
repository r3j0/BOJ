import sys
input = sys.stdin.readline

visited = {}
visited["0_0"] = 1
n = int(input().rstrip())
ny = 0
nx = 0

string = input().rstrip()
for s in string:
    if s == 'N': 
        visited[str(ny+1)+"_"+str(nx)] = 1
        ny += 1
    elif s == 'S': 
        visited[str(ny-1)+"_"+str(nx)] = 1
        ny -= 1
    elif s == 'E': 
        visited[str(ny)+"_"+str(nx+1)] = 1
        nx += 1
    else: 
        visited[str(ny)+"_"+str(nx-1)] = 1
        nx -= 1

print(len(visited))