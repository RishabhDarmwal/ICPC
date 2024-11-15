

# # Read an integer
n=int(input())
for _ in " "*n:
    N,A,B,C,D,P,Q,Y=map(int,input().split())
    X=list(map(int,input().split()))
    if A<C and B>D and P<Q: #train is in between
        time=abs(C-A)*P
        if time<=Y:
            time+=(Y-time)  #waiting for train
            time+=(D-C)*Q +(B-D)*P
            
        else:
            time+=(B-C)*P
        print(min(abs(B-A)*P,time))
            
    else:
        print(abs(B-A)*P)

# t = int(input())
# for _ in range(t):
#     n,a,b,c,d,p,q,y = map(int,input().split())
#     x = list(map(int,input().split()))
#     x.insert(0,0)
#     train = None
#     if abs(x[a]-x[c])*p <= y:
#         wait = y-abs(x[a]-x[c])*p
#         train=(abs(x[c]-x[a])*p)+(abs(x[d]-x[c])*q)+(abs(x[b]-x[d])*p)+wait 
#     walk = abs(x[b]-x[a])*p
#     if train:
#         print(min(walk,train))
#     else:
#         print(walk)
