n=int(input())
l=list(map(int,input().split()))
sum1=sum(l)
if(sum1<3 or sum1%3!=0):
    print(0)
else:
    count=0
    W=sum1//3
    l1 = [[0 for i in range(n+1)] for j in range(W+1)]
    for i in range(1, W+1):
        for j in range(1, n+1):
            l1[i][j] = l1[i][j-1]
            if(l[j-1]<=i):
                x = l1[i-l[j-1]][j-1]+l[j-1]
                if(x > l1[i][j]):
                    l1[i][j] = x
            if(l1[i][j] == W):
                count+=1

    if(count < 3):
        print(0)
    else:
        print(1)
    
