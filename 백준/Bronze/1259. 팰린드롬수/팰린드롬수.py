while True:
    n = input()
    if n == "0": break
    n = list(n)

    print('yes' if n == n[::-1] else 'no')