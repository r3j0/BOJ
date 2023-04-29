import sys
input = sys.stdin.readline

t = input().rstrip()
p = input().rstrip()

def kmp(all_string, pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    # kmp table
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]
        
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j-i+2)
                i = table[i-1]

    return result

res = kmp(t, p)
print(len(res))
print(' '.join(map(str, res)))