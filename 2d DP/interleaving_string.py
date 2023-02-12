#total number of chrater must match in s1+s1=s3
#relative order has to be maintained
def isInterleave(s1,s2,s3):
    dp=[[False]*(len(s2)+1) for i in range(len(s1)+1)]
    dp[len(s1)][len(s2)]=True
    for i in range(len(s1),0,-1):
        for j in range(len(s2),0,-1):
            if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                dp[i][j]= True
            if j < len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                dp[i][j]= True
    return dp[len(s1)][len(s2)]
x=isInterleave("aabcc","dbbca","aadbbcbcac")
print(x)
