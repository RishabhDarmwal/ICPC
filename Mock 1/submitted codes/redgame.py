for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    go_on=1
    while go_on:        
        nums=[(num,idx) for idx,num in enumerate(a) if num>k]        
        if len(nums)<2:
            go_on=0
        else:
            nums.sort()
            req_nums=nums[:2]
            inds=[ele[1] for ele in req_nums]            
            a[inds[0]]-=1
            a[inds[1]]-=1
            a.sort(reverse=True)
            
    print(sum(a))