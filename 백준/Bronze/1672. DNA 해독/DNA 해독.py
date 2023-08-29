import sys
input = sys.stdin.readline

dna = {
    'AA':'A', 'AG':'C', 'AC':'A', 'AT':'G',
    'GA':'C', 'GG':'G', 'GC':'T', 'GT':'A',
    'CA':'A', 'CG':'T', 'CC':'C', 'CT':'G',
    'TA':'G', 'TG':'A', 'TC':'G', 'TT':'T'
}

n = int(input().rstrip())
string = input().rstrip()
if len(string) == 1:
    pass
elif len(string) == 2:
    string = dna[string]
else:
    now = string[-2:]
    string = string[:-2]

    for i in range(len(string) - 1, -1, -1):
        now = string[i] + dna[now]
    
    string = dna[now]

print(string)