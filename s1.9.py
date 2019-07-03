n,k=map(int,input().split())
a=list(map(int,input().split()))
b=0
d=0
while(b<k):
   d+=a[b]
   b+=1
print(d)
