m,n=map(int,input().split())
p=0
c=1
for i in range(10*10):
    p,c=c,(p+c)%10
    if(p==0 and c==1):
        x=i+1
        break
count1=0
count2=0
p=0
c=1
n=n%x
m=m%x
for i in range(n):
    count1+=c
    p,c=c,(p+c)
p=0
c=1    
for i in range(m-1):
    count2+=c
    p,c=c,(p+c)
ans=count1-count2
ans=ans%10
print(ans)
