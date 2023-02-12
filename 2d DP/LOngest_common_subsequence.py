t1='abcde'
t2='ace'
#common_sequace with length=3
dp=[[0 for j in range(len(t2)+1)]for i in range(len(t1)+1)]
for i in range(len(t1)-1,-1,-1):
    for j in range(len(t2)-1,-1,-1):
        if t1[i]==t2[j]:
            dp[i][j]=1+dp[i+1][j+1]#dp[i+1][j+1] gives the diagonal element
        else:
            dp[i][j]=max(dp[i][j+1],dp[i+1][j])
print(dp[0][0])
