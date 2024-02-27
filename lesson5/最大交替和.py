n=int(input())
a=list(map(int,input().split()))
add=[]
sub=[]
for i in range(n):
    if i%2==0:
        add.append(abs(a[i]))
    else:
        sub.append(abs(a[i]))
ans=sum(add)-sum(sub)
if(n==1):
    print(add[0])
else:
    if max(sub)>min(add):#由于max/min后的列表不能为空，所以前面必须对n==1的情况进行单独讨论
        ans+=2*max(sub)-2*min(add)
    print(ans)

    


