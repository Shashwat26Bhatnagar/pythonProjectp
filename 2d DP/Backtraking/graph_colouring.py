n=5
adj=[[]]
for i in range(n):
    for j in range(n):
        adj[i][j]=input("enter the adjancey patrix")
m=5
color=[]*n
def is_safe(v:int,c:int):
    for k in range(n):
        if adj[v][i]==1 and c==color[i]:
            return False
def solve(v:int):