import sys
input = sys.stdin.readline

n1, n2 = map(int, input().rstrip().split())
print(100-n1, 100-n2, 100-(100-n1+100-n2), (100-n1)*(100-n2), ((100-n1)*(100-n2))//100, ((100-n1)*(100-n2))%100)
print((100-(100-n1+100-n2))+((100-n1)*(100-n2))//100, ((100-n1)*(100-n2))%100)