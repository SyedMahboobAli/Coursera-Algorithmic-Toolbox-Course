n = int(input())
sequence =[]
if(n==1):
    sequence = [1]
else:
    dp = [0,0]
    for i in range(2,n+1):
        if(i%2==0 and i%3==0):
            dp.append(min(dp[int(i/2)],dp[int(i/3)],dp[i-1])+1)
        elif(i%2==0):
            dp.append(min(dp[int(i/2)],dp[i-1])+1)
        elif(i%3==0):
            dp.append(min(dp[int(i/3)],dp[i-1])+1)
        else:
            dp.append(dp[i-1]+1)
    sequence = [n]
    value = dp[n]-1
    for i in range(n-1,1,-1):
        if(dp[i]==value):
            sequence.append(i)
            value-=1
    sequence.append(1)
    sequence=sequence[::-1]
print(len(sequence) - 1)
for i in sequence:
    print(i, end=' ')
