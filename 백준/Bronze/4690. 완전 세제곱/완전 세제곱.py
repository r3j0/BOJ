
for a in range(2, 101):
    na = a**3
    for b in range(2, 101):
        nb = b**3
        if na < nb:
            continue
        for c in range(b, 101):
            nc = c**3
            if na < nb + nc:
                continue
            for d in range(c, 101):
                nd = d**3
                if na < nb + nc + nd:
                    continue
                elif na == nb + nc + nd:
                    print('Cube = %d, Triple = (%d,%d,%d)'%(a, b, c, d))