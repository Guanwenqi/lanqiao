t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    if a==1:
        if(n-1)%b==0:
            print("Yes")
        else:
            print("No")
    else:
        cnt=1
        flag=False
        while cnt<=n:
            if(n-cnt)%b==0:
                flag=True
            cnt*=a
        if flag:
            print("Yes")
        else:
            print("No")
           
