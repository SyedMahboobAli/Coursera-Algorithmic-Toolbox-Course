n,c=map(int,input().split())
x=dict()
v=0
for i in range(n):
    v1,w1=map(int,input().split())
    a=[v1,w1]
    y=v1/w1
    x[y]=a
for i in sorted(x.keys(),reverse=True):
    if(c>x[i][1]):
        c-=x[i][1]
        v+=x[i][0]
    else:
        v=v+(x[i][0]*(c/x[i][1]))
        break
print(format(v,'.4f'))
    
