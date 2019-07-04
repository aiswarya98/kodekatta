def prim(k):
    c=0
    for i in range(2,k):
        if(k%i==0):
            c=1
            break
    else:
        print(k,end=" ")     
a,b=map(int,input().split())
l=[]
for j in range(a+1,b):
    prim(j)
    
