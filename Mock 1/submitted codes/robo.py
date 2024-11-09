for _ in range(int(input())):
    s = input().strip()
    
    floor=[0]*len(s)
    safe = True
    for i in range(len(s)):
        if s[i]=='.':
            continue
        else:
            move=int(s[i])

            for j in range(max(0, i - move),min(len(s), i + move + 1)):
                
                floor[j]+=1
                if floor[j] > 1:
                    safe = False
                    break
        if not safe:
            break
    if safe:
        print("safe")
    else:
        print("unsafe")
           


