while True:#未知数量的测试样例
    try:
        n,m=map(int,input().split())
        li=list(map(int,input().split()))
        diff=[0]*(n+1)
        diff[0]=li[0]
        for i in range(1,n):
            diff[i]=li[i]-li[i-1]
        for i in range(m):
            x,y,z=map(int,input().split())
            x,y=x-1,y-1
            diff[x]+=z
            diff[y+1]-=z
        li[0]=diff[0]
        for i in range(1,n):
            li[i]=li[i-1]+diff[i]
        print(' '.join(map(str,li)))
    except:
        break
    