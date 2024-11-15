from collections import Counter
n,m=map(int,input().split())
red=[]
blue=[]
for _ in " "*(n):
    x,vi=map(int,input().split())
    red.append(x*vi)
for _ in " "*(m):
    y,vj=map(int,input().split())
    blue.append(y*vj)

common_count = sum((Counter(red) & Counter(blue)).values())
print(common_count) 