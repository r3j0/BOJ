import sys
input = sys.stdin.readline

hp_player, atk_player, hp_enemy, atk_enemy = map(int, input().split())
p, s = map(int, input().split())

if 1 <= hp_enemy % atk_player <= p or 1 <= hp_enemy - (atk_player * (hp_enemy // atk_player - 1)) <= p: atking_player = (hp_enemy + s) // atk_player + (1 if (hp_enemy + s) % atk_player != 0 else 0)
else: atking_player = hp_enemy // atk_player + (1 if hp_enemy % atk_player != 0 else 0)
atking_enemy = hp_player // atk_enemy + (1 if hp_player % atk_enemy != 0 else 0)

if atking_enemy < atking_player: print('gg')
else: print('Victory!')