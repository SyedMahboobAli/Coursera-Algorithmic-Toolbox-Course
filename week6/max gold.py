W,n= map(int,input().split())
w=list(map(int,input().split()))
a = [[0 for _ in range(W+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, W+1):
        if(i == 0 or j == 0):
            a[i][j] = 0
        elif(w[i-1] <= j):
            a[i][j] = max(a[i-1][j], a[i-1][j-w[i-1]]+w[i-1])
        else:
            a[i][j] = a[i-1][j]
print(a[-1][-1])
