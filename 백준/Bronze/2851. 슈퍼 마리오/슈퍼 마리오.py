now = 0
done = 0
for _ in range(10):
    n = int(input())
    if done == 1: continue
    if abs(100-now) < abs(100-(now+n)):
        done = 1
        continue
    else:
        now += n
print(now)