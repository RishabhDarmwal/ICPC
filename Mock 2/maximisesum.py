for _ in ' '*int(input()):
    n=int(input())
    a=list(map(int,input().split()))
    sum=0
    x=sorted(a,reverse=True)
    y=sorted(a)
    l=len(a)
   
    for i in range(l//2):
        sum+=abs(y[i]-x[i])
        
    print(sum)

