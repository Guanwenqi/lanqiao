import sys
sys.setrecursionlimit(1000000)
def update(path):
    global res
    st=list(map(int,list(s)))
    for pa in path:
        pa=op[pa]
        if pa[0]==1:
            st[pa[1]]+=pa[2]
            st[pa[1]]%=10
        else:
            st[pa[1]],st[pa[2]]=st[pa[2]],st[pa[1]]
        if ''.join(list(map(str,st)))==t:
            res=True
def dfs(u):
    if res==True:
        return
    if u==k:
        update(path)
        return
    for i in range(k):
        if not vis[i]:
            vis[i]=True
            path.append(i)
            dfs(u+1)
            vis[i]=False
            path.pop(-1)
    dfs(k)#前面一旦pop出来，就直接进到update里面，完成排列+子集的双重操作
n=int(input())
s=input()
t=input()
k=int(input())
op=[]
for i in range(k):
    op.append(list(map(int,input().split())))
vis=[False]*k
path=[]
res=False
dfs(0)
print("Yes") if res else print("No")