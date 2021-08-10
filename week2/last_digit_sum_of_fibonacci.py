n=int(input())
p=0
c=1
for i in range(10*10):
    p,c=c,(p+c)%10
    if(p==0 and c==1):
        x=i+1
        break
count=0
p=0
c=1
n=n%x
for i in range(n):
    count+=c
    p,c=c,(p+c)
print((count)%10)
