a=input()
l=int(len(a))
d=[]
for i in a:
    d.append(int(i)**3)
b=0
c=0
while(c<l):
    b+=d[c]
    c+=1
if(b==int(a)):
    print("yes")
else:
    print("no")
