n,m,q=map(int,input().split())
diff=[[0 for i in range(m+2)] for j in range(n+2)]
def pro(x1,y1,x2,y2,c):
    diff[x1][y1]+=c
    diff[x1][y2+1]-=c
    diff[x2+1][y1]-=c
    diff[x2+1][y2+1]+=c
for i in range(1,n+1):
    tmp=[0]+list(map(int,input().split()))
    for j in range(1,m+1):
        pro(i,j,i,j,tmp[j])
for i in range(q):
    x1,y1,x2,y2,c=map(int,input().split())
    pro(x1,y1,x2,y2,c)
for i in range(1,n+1):
    for j in range(1,m+1):
        diff[i][j]+=diff[i-1][j]+diff[i][j-1]-diff[i-1][j-1]
    print(*diff[i][1:-1])
    
