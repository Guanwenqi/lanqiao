n,m,k=map(int,input().split())
left,right=1,n*m
def check(x):
    cnt=0
    for i in range(1,n+1):
        cnt+=min(m,x//i)
    return cnt
ans=0
while left<=right:
    mid=(left+right)//2
    if check(mid)>=k:
        ans=mid
        right=mid-1
    else:
        left=mid+1
print(ans)
# 注意：当处理“第k小问题”，“最大值最小化”，“单调的暴力枚举”时，应考虑二分答案