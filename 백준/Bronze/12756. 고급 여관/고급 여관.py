import sys
input = sys.stdin.readline

a_atk, a_hp = map(int, input().rstrip().split())
b_atk, b_hp = map(int, input().rstrip().split())

while a_hp > 0 and b_hp > 0:
    a_hp -= b_atk
    b_hp -= a_atk

if a_hp <= 0 and b_hp <= 0: print("DRAW")
elif a_hp <= 0: print("PLAYER B")
else: print("PLAYER A")