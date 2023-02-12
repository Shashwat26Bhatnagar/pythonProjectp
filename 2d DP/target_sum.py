#things to keep in mind
# 1)outofbounds condition=when index become greater or equal to len(nums)
# 2)total is the maximum number possible from given num array that is 5 in our case

nums=[1,1,1,1,1]
target=3
def findTargetSumWays(nums,target):
    dp={}#(index,total)
    def backtrack(i,total):
        if i==len(nums):
            return 1 if total==target else 0
        if(i,total) in dp:
            return dp[(i,total)]
        dp[(i,total)]=backtrack(i+1,total+nums[i])+backtrack(i+1,total-nums[i])