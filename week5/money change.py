m=int(input())
n=[1,3,4]
if(m<3):
    print(m)
elif(m==3 or m==4):
    print(1)
else:
    dp = [0,1,2,1,1]
    for i in range(5,m+1):
        dp.append(min(dp[i-1],dp[i-3],dp[i-4])+1)
    print(dp[-1])
