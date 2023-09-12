while True:
    try:
        a, b = map(int, input().rstrip().split())
    except:
        break
    
    print("%.2f"%(a/b))