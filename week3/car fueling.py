d=int(input())
m=int(input())
n=int(input())
l=list(map(int,input().split()))
l.append(0)
l.append(d)
l.sort()
c=0
f=0
m1=m
for i in range(1,len(l)):
    if(i==len(l)-1):
       x=l[i]-l[i-1]
       if(x>m):
           f=1
       else:
           continue
    else:
        x=l[i]-l[i-1]
        y=l[i+1]-l[i]
        if(x>m):
            f=1
            break
        if(x+y<=m):
            m=m-x
            continue
        elif(x+y>m):
            c+=1
            m=m1
if(f!=1):
    print(c)
else:
    print(-1)
       
   

    
