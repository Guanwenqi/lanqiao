string="www.nju.edu.cn"
# u1,u2,u3=string.split('.',2)#以'.'为分隔符，分2次
# print(u1)
# print(u2)
# print(u3)
u4=string.split('.',3)[3]#以'.'为分隔符，分3次，取出下标为3的片段
print(u4)
# a=input("请输入一串数字，以空格分割")
# lst=a.split()#默认为以空格为分隔符，但分隔符不能为空，即（''）
# print(lst)
# n=int(input())
# cnt=0
# a,b,c=map(int,input().split())
# for i in range(1,n+1,1):
#   if i%a!=0 and i%b!=0 and i%c!=0:
#     cnt+=1
# print(cnt)
# n=int(input())
# sum=0
# for i in range(1,n+1):
#   i=str(i) 
#   if '2' in i or '0' in i or '1' in i or '9' in i:
#     sum+=i
# print(sum)