import heapq
n=int(input())
a=list(map(int,input().split()))
heapq.heapify(a)#动态寻找最小值时用堆
ans=0
while len(a)>=2:
    x=heapq.heappop(a)
    y=heapq.heappop(a)
    heapq.heappush(a,x+y)
    ans+=(x+y)
print(ans)