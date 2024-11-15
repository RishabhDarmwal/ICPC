# from collections import Counter
# for _ in " "*int(input()):
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     c=Counter(a).values()
#     C=[i for i in c if i>1]
#     if len(C)==0:
#         print((n*(n-1))//2)
#     else:        
#         ans=(n*(n-1))//2-sum([(l*(l-1))//2 for l in c])
#         while len(C)>0:
#             val=max(C)-1
#             ans+=val
#             C.remove(max(C))
#             if val>0:
#                 C.append(val)
#         print(ans)
t=int(input())

for _ in range(t):

    n,k=map(int,input().split())

    l=list(map(int,input().split()))

    d={}

    for i in l:

        try:

            d[i]+=1

        except:

            d[i]=1

    ans=0

    x=list(d.values())

    c=sum(x)

    for i in x:

        c-=i

        ans=ans+c*i

    x.sort(reverse=True)

    d=x[0]

    for j in range(1,len(x)):

        if k==0:

            break

        if x[j]==d:

            pass

        a=x[j]

        b=d-1

        n=(b-a+1)*j

        if n>k:

            c=k//j

            b=d-1

            a=b-c+1

            s=((a+b)*c)//2

            ans+=s*j

            c=k%j

            ans+=(a-1)*c

            k=0

            break

            

        

        s= ((a+b)*n)//2

        ans+=s

        d=x[j]

        k-=n

    if k==0:

        print(ans)

        continue

    if d==1:

        print(ans)

        continue

    n=len(x)

    x=k//n

    if x>=d-1:

        b=d-1

        s=(b*(b+1))//2

        ans+=s*n

        print(ans)

    else:

        b=d-1

        a=b-x+1

        s=((a+b)*x)//2

        ans+=s*n

        x=k%n

        c=(a-1)*x

        print(ans+c)

        

        

        

