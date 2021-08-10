n,m=map(int,input().split())
p=0
c=1
for i in range(m*m):
    p,c=c,(p+c)%m
    if(p==0 and c==1):
        x=i+1
        break
n=n%x
p=0
c=1
if(n==0):
    print(p)
elif(n==1):
    print(c)
else:
    for i in range(n-1):
        p,c=c,(p+c)
    print(c%m)
