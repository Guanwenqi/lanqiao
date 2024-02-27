row,col=map(int,input().split())
x,y=map(int,input().split())
ans=[[0]*col for i in range(row)]
value=1
m,n=0,0
ans[m][n]=value
while value<row*col:
    while n+1<col and ans[m][n+1]==0:
        value+=1
        n+=1
        ans[m][n]=value
    while m+1<row and ans[m+1][n]==0:
        value+=1
        m+=1
        ans[m][n]=value
    while n-1>=0 and ans[m][n-1]==0:
        value+=1
        n-=1
        ans[m][n]=value
    while m-1>=0 and ans[m-1][n]==0:
        value+=1
        m-=1
        ans[m][n]=value
print(ans[x-1][y-1])