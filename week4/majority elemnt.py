n=int(input())
l=list(map(int,input().split()))
d={}
f=0
for i in range(len(l)):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]]=1
for i in d:
    if(d[i]>n//2):
        f=1
        break
if(f==1):
   print(1)
else:
   print(0)

