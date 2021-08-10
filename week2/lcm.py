x,y=map(int,input().split())
m=max(x,y)
n=m
while(1):
    if(m%x==0 and m%y==0):
        break
    m=m+n
print(m)    
