n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

# 找出最长公共子序列的过程是回溯，由于路径不同，找出序列可能不同，但长度恒定
# ans=[]
# x,y=n,m
# while x!=0 and y!=0:
#     if dp[x][y]==dp[x-1][y-1]:
#         x=x-1
#     elif dp[x][y]==dp[x][y-1]:
#         y=y-1
#     else:
#         ans.append(a[x])
#         x,y=x-1,y-1
# print(ans[::-1])