n=int(input())
a=[]
for i in range(n):
    a1,b1=map(int,input().split())
    x=[a1,b1]
    a.append(x)
a.sort(key=lambda x:x[1])
b=[a[0][1]]
for i in range(1,n):
    if(a[i][0]<=b[-1]):
        continue
    else:
        b.append(a[i][1])
print(len(b))
for i in b:
    print(i,end=' ')


    
    
