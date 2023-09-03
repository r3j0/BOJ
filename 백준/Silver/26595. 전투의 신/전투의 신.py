import sys
input = sys.stdin.readline

n = int(input().rstrip())
a, pa, b, pb = map(int, input().rstrip().split())

now_a = n // pa
now_b = (n - (now_a * pa)) // pb
change = n - (now_a * pa + now_b * pb)
max_battle = now_a * a + now_b * b
max_a = now_a
max_b = now_b
while now_a > 0:
    now_a -= 1
    change += pa
    now_b += change // pb
    change %= pb 
    if max_battle < now_a * a + now_b * b:
        max_battle = now_a * a + now_b * b
        max_a = now_a
        max_b = now_b

print(max_a, max_b)