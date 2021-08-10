n=int(input())
l=list(map(int,input().split()))
num1=0
num2=0
maxindex1=-1
maxindex2=-1
for i in range(n):
    if(maxindex1==-1 or num1<l[i]):
        maxindex1=i
        num1=l[i]
for j in range(n):
    if(j!=maxindex1 and (maxindex2==-1 or num2<l[j])):
        num2=l[j]
        maxindex2=j
print(num1*num2 )
