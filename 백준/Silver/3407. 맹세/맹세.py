arr = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
'Cs', 'Ba',	'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
'Fr', 'Ra',	'Rf', 'Db',	'Sg', 'Bh',	'Hs', 'Mt', 'Ds', 'Rg',	'Cn', 'Fl', 'Lv',	 	 
'La', 'Ce', 'Pr', 'Nd',	'Pm', 'Sm',	'Eu', 'Gd',	'Tb', 'Dy',	'Ho', 'Er',	'Tm', 'Yb',	'Lu',
'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
dic = {}
for s in arr:
    now = s.lower()
    dic[now] = 1

import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    string = input().rstrip()

    dp = [0 for _ in range(len(string))]
    for i in range(len(string)):
        if i == 0:
            if dic.get(string[i]):
                dp[0] = 1
            if len(string) > 0 and dic.get(string[i]+string[i+1]):
                dp[1] = 1
        else:
            if dic.get(string[i]):
                dp[i] = max(dp[i], dp[i-1])
            if i + 1 < len(string) and dic.get(string[i]+string[i+1]):
                dp[i+1] = max(dp[i+1], dp[i-1])
    
    #print(dp)
    print('YES' if dp[-1] == 1 else 'NO')