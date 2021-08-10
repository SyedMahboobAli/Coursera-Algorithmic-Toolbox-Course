n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
a.sort(reverse=True)
b.sort(reverse=True)
for i in range(len(a)):
    c+=a[i]*b[i]
print(c)
