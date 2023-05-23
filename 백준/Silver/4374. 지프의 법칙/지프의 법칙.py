

while True:
    try:
        dic = {}
        lis = []
        n = int(input())
        while True:
            strinput = input()
            if strinput == "EndOfText":
                break
            
            strrr = ""
            for s in range(len(strinput)):
                if 'a' <= strinput[s] <= 'z' or 'A' <= strinput[s] <= 'Z': strrr += strinput[s]
                else: 
                    if strrr != '':
                        strrr = strrr.lower()
                        if dic.get(strrr, 0) == 0:
                            dic[strrr] = 1
                        else:
                            dic[strrr] += 1
                        strrr = ''
            
            if strrr != '':
                strrr = strrr.lower()
                if dic.get(strrr, 0) == 0:
                    dic[strrr] = 1
                else:
                    dic[strrr] += 1
        
       # print("Searching...")
        for i in dic:
            #print(i, dic[i])
            if dic[i] == n:
                lis.append(i)
        
        #print()
        if len(lis) == 0:
            print("There is no such word.")
        else:
            lis.sort()
            for a in lis:
                if a != '':
                    print(a)
        print()
    except:
        break
