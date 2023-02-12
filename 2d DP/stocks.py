# transaction_e.g=[buy,sell,cooldown,sell]
price_of_stock=[1,2,3,0,2]
#if buy->i+1
#if sell->i+2//cooldown
def maxProfit(price_of_stock):
    dp={}#keys=(i,bouying) value=max_profit
    def dfs(i,buying):
        if i>=len(price_of_stock):
            return 0
        if (i,buying) in dp:
            return dp[(i,buying)]
        if buying:
            buy=dfs(i+1,not buying)-price_of_stock[i]
            cooldown= dfs(i+1,buying)
            dp[(i,buying)]=max(buy,cooldown)
        else:
            sell=dfs(i+2,not buying)+price_of_stock[i]
            cooldown= dfs(i+1,buying)
            dp[(i,buying)]=max(sell,cooldown)
        return dp[(i,buying)]
    return dfs(0,True)
