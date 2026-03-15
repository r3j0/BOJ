# 2263 : 트리의 순회
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input().rstrip())
inorder = list(map(int, input().rstrip().split()))
poorder = list(map(int, input().rstrip().split()))

# 중위 순회가 주어지고
# 후위 순회가 주어졌을 때

# 전위 순회를 구해라.

# 1. 요소를 하나씩 잡고, 그 요소가 다른 배열에 등장할 때까지를 구간으로 나누고,
#    [ 루트 ] - left - [ 루트 ] - left - [ 루트 ] 로 잡는다.
# 2. 분할했을 때 in맨앞 = po맨뒤 라면 [ 그 원소 ] - right [ 트리 ] 로 잡는다.

tree = [[-1, -1] for _ in range(n+1)]

def divideTree(iIdx, pIdx):
    selected = -1
    previous_root = -1
    if iIdx[1] - iIdx[0] == pIdx[1] - pIdx[0] == 0:
        return inorder[iIdx[0]]

    if inorder[iIdx[0]] == poorder[pIdx[1]]:
        right_root = iIdx[0]
        new_i = [iIdx[0] + 1, iIdx[1]]
        new_p = [pIdx[0], pIdx[1] - 1]
        tree[inorder[right_root]][1] = divideTree(new_i, new_p)
        return inorder[right_root]

    length = iIdx[1] - iIdx[0] + 1
    for i in range(length):
        if selected == -1:
            selected = i
        
        if poorder[pIdx[0] + i] == inorder[iIdx[0] + selected]:
            new_i = [iIdx[0] + selected, iIdx[0] + i]
            new_p = [pIdx[0] + selected, pIdx[0] + i]
            now_root = divideTree(new_i, new_p)
            tree[now_root][0] = previous_root
            previous_root = now_root

            selected = -1

    # 루트를 리턴
    return previous_root

root = divideTree([0, n - 1], [0, n - 1])

ans = []
def preSearch(now):
    ans.append(now)
    for i in range(2):
        if tree[now][i] != -1:
            preSearch(tree[now][i])

preSearch(root)

print(' '.join(map(str, ans)))