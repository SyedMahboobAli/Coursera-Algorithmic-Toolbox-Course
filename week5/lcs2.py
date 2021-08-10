def lcs2(a, b):
    n1 = len(a)
    n2 = len(b)
    dp = []
    for i in range(n2+1):
        dp.append([0]*(n1+1))
    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if(a[j-1]==b[i-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n2][n1]

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
print(lcs2(a, b))
