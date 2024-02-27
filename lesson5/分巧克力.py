n,k=map(int,input().split())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y))
def check(x):
    cnt=0
    for h,w in a:
        cnt+=(h//x)*(w//x)
    return cnt>=k
left,right=1,100000
ans=1
while left<=right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid-1
print(ans)