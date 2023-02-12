#2-D dp is bottom-up approach
#only down and right  step are legal
#result =right+down
from typing import List

# class Solution:
#     def uniquePaths(self,m:int,n:int)->int:
#         row=[1]*n
#         for i in range(m-1):
#             newRow=[1]*n
#             for j in range(n-2,-1,-1):
#                 newRow[j]=newRow[j+1]+row[j]
#             row = newRow
#         return row[0]

t=int(input())
def uniquepath(r:int,c:int)->int:
        dp: list[list[int]]=[[0]*c for i in range(r)]
        for i in range(1,r+1):
            for j in range(1,c+1):
                if i==0 or j==0:
                    dp[i][j]=1
               else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp[-1][-1])