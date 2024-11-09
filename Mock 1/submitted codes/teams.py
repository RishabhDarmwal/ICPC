#tookhelp
def better(a,b):
    h=False
    for x,y in zip(a,b):
        if x<y:
            return False
        if x>y:
            h=True
    return h

def sort(t1,t2,t3):
    p=[(t1,t2,t3),(t1,t3,t2),(t2,t1,t3),(t2,t3,t1),(t3,t1,t2),(t3,t2,t1)]
    for x in p:
        if better(x[1],x[0]) and better(x[2],x[1]):
            return "yes"
    return "no"

for _ in range(int(input())):
    a=tuple(map(int,input().split()))
    b=tuple(map(int,input().split()))
    c=tuple(map(int,input().split()))
    print(sort(a,b,c))
