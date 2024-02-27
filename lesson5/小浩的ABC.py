def printf(x):
    if x==1:
        print(-1)
    elif x<=1e6+1:
        print(x-1,1,1)
    else:
        if x%1e6==0:
            print(int(1e6),int(x//1e6)-1,int(1e6))
        else:
            print(int(1e6),int(x//1e6),int(x%1e6))
t=int(input())
for i in range(t):
    x=int(input())
    printf(x)