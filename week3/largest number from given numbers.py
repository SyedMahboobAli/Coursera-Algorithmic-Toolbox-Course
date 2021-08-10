n=int(input())
l1=list(input().split())
l2=[]
length=len(max(l1))
length+=1
for i in l1:
    temp=i*length
    x=temp[:length]
    t=(x,i)
    l2.append(t)
l2.sort(reverse=True)
s=""
for i in range(len(l2)):
    s+=l2[i][1]
print(s)
    
