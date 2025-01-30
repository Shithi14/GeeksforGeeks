#https://www.geeksforgeeks.org/problems/radix-sort/
def radix(a,pos):
    n=len(a)
    carr=[0]*10
    for i in a:
        d=(i//pos)%10
        carr[d]+=1
    
    for i in range(1,len(carr)):
        carr[i]+=carr[i-1]

    out=[0]*n
    for i in range(n-1,-1,-1):
        d=(a[i]//pos)%10
        out[carr[d]-1]=a[i]
        carr[d]-=1
    
    for i in range(0,n):
        a[i]=out[i]
    


def ra(a):
    M=max(a)
    pos=1
    while M//pos>0:
        radix(a,pos)
        pos*=10
    
    return a
 

a=[33,2,6666,35,99]
f=ra(a)
print(f)