# print("hello","world",123)
# #默认空格分隔，换行结束
# print("hello","world",123,sep='_')
# #以sep分隔
# print("hello","world",123,end="?")
# print("hello","world",123,sep='_')
# '''单双引号可以互换
# end表示以什么结尾'''
n=int(input())
pas=0
exe=0
a=[]
for i in range(n):
  a[i]=int(input())
  if a[i]>=60:
    pas+=1
    if a[i]>=85:
      exe+=1
print(int(pas/n+0.5),'%')
print(int(exe/n+0.5),'%')