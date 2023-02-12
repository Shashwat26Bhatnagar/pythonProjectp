class Item:
    def __init__(self,wt,val):
        self.wt=wt
        self.val=val
        self.cost=val/wt
    def __lt__(self,other):
        return self.cost<other.cost
class FractionalKnapsack:
    def getMaxValue(self,wt,val,cap):
        arr=[]
        for i in range(len(wt)):
            arr.append(Item(wt[i],val[i],i))
        arr.sort(reverse=True)
        ans=0
        for i in arr:
            currwt=int(i.wt)
            currvl=int(i.val)
            if(currwt<cap):
                ans=ans+currvl
                cap=cap-currwt
            else:
                currcost=currvl/currwt
                ans=ans+cap*currcost
                break
        return ans

st1=input()
v=st1.split()
val=[int(i) for i in v]

str2=input()
w=str2.split()
wt=[int(j) for j in w]
cap=int(input)
maxvalue=FractionalKnapsack.getMaxValue(wt,val,cap)
print(maxvalue)