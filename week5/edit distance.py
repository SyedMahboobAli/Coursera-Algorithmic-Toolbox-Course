s=input()
t=input()
dp = []
n1 = len(s)
n2 = len(t)
for i in range(n2+1):
    dp.append([0]*(n1+1))
for i in range(1,n1+1):
    dp[0][i] = dp[0][i-1]+1
for i in range(1,n2+1):
    dp[i][0] = dp[i-1][0]+1
for i in range(1,n2+1):
    for j in range(1,n1+1):
        if(s[j-1]==t[i-1]):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
print(dp[n2][n1])
