# 顺子时间（2022年）
# import datetime
# start=datetime.date(2022,1,1)
# end=datetime.date(2022,12,31)
# ans=0
# while start<=end:
#     now_date=start.strftime("%Y%m%d")
#     if '012' in now_date or '123' in now_date:
#         ans+=1
#     start+=datetime.timedelta(days=1)
# print(ans)

# s=[123,456,789]
# print(' '.join(map(str,s)))
n=int(input())
a=list(map(int,input().split()))
a.sort()
minvalue=abs(a[0]-a[1])
for i in range(1,n-1):
  if abs(a[i]-a[i+1])<minvalue:
    minvalue=abs(a[i]-a[i+1])
print(minvalue)


