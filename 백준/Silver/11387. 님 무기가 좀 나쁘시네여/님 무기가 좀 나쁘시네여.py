import sys
import decimal
input = sys.stdin.readline

cri_weapon = list(map(int, input().rstrip().split()))
pabo_weapon = list(map(int, input().rstrip().split()))
weapon_for_cri = list(map(int, input().rstrip().split()))
weapon_for_pabo = list(map(int, input().rstrip().split()))

cri = []
pabo = []

for i in range(5):
    cri.append(cri_weapon[i] - weapon_for_cri[i])
    pabo.append(pabo_weapon[i] - weapon_for_pabo[i])

for i in range(5):
    cri[i] += weapon_for_pabo[i]
    pabo[i] += weapon_for_cri[i]

def battlePower(status):
    status[1] += 100
    status[4] += 100
    s1 = decimal.Decimal('%d.%02d'%(status[1]//100, status[1]%100))
    s2 = decimal.Decimal('0.%02d'%status[2])
    if status[2] >= 100:
        s2 = decimal.Decimal('1.0')
    s3 = decimal.Decimal('%d.%02d'%(status[3]//100, status[3]%100))
    s4 = decimal.Decimal('%d.%02d'%(status[4]//100, status[4]%100))
    return float(decimal.Decimal('%d.0'%(status[0])) * (s1) * ((decimal.Decimal('1.0') - s2) + (s2 * s3)) * (s4))

cri_first = battlePower(cri_weapon)
cri_second = battlePower(cri)
pabo_first = battlePower(pabo_weapon)
pabo_second = battlePower(pabo)

def printPower(a, b):
    if a < b: print('+')
    elif a == b: print('0')
    else: print('-')

printPower(cri_first, cri_second)
printPower(pabo_first, pabo_second)