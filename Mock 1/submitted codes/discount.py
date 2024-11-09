#tookhelp
def minprice(N):
    if N<10:
        return N 
    nstr = str(N)
    l=len(nstr)
    mprice = float('inf')
    for i in range(l):

        new_num = nstr[:i] + nstr[i+1:]

        price = int(new_num)
        mprice = min(mprice, price)
    
    return mprice


for _ in range(int(input())):
    N = int(input())
    result = minprice(N)
    print(result)