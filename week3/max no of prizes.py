n=int(input())
l=[]
s=0
f=1
if(n==1):
    f=0
for i in range(1,n):
   s=s+i
   if(s>n):
       break
   if(s==n):
       l.append(i)
       f=0
       break
   else:
       l.append(i)
if(f==1):
    x=l.pop()
    if(x==1 or x==2):
        x-=1
    l.append(n-sum(l))
if(n==1):
    l.append(1)
print(len(l))
for i in l:
    print(i,end=' ')
