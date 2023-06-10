now = []
now.append(int(input()))
flat = []
for _ in range(3):
    now.append(int(input()))
    flat.append(now[-1] - now[-2])

if flat[0] == flat[1] == flat[2] == 0: print('Fish At Constant Depth')
elif min(flat) > 0: print('Fish Rising')
elif max(flat) < 0: print('Fish Diving')
else: print('No Fish')