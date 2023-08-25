import sys
input = sys.stdin.readline

word = {
    "A":"000000",
    "B":"001111",
    "C":"010011",
    "D":"011100",
    "E":"100110",
    "F":"101001",
    "G":"110101",
    "H":"111010"
}

n = int(input().rstrip())
string = input().rstrip()
result = ""
done = 0
for i in range(n):
    now_word = ''
    if i == n - 1:
        now_word = string[i*6:]
    else:
        now_word = string[i*6:(i+1)*6]

    dif_one = []
    dif_two = []
    found = 0
    for k, v in word.items():
        if v == now_word:
            result += k
            found = 1
            break
        else:
            dif = 0
            for ii in range(6):
                if v[ii] != now_word[ii]:
                    dif += 1
            
            if dif == 1:
                dif_one.append(k)
            else:
                dif_two.append(k)

    if found == 0 and done == 0:
        if len(dif_one) == 1:
            result += dif_one[0]
        else:
            done = i+1

if done != 0: print(done)
else: print(result)