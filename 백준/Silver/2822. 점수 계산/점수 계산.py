prob = []
for i in range(8):
    prob.append([int(input()), i])

prob.sort(key=lambda x:-x[0])
print(prob[0][0] + prob[1][0] + prob[2][0] + prob[3][0] + prob[4][0])
print(' '.join(map(str, sorted([prob[0][1]+1, prob[1][1]+1, prob[2][1]+1, prob[3][1]+1, prob[4][1]+1]))))