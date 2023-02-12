class item:
    def __init__(self,wt,val,index):
        self.wt=wt
        self.val=val
        self.index=index
        self.cost=val/wt
    def _lt_(self,other):
        return self.cost<other.cost
class Fractional_