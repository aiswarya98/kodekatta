aj=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(aj):
    print(a[i],end=" ")
