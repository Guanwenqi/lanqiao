# def merge(A,B):
#   result=[]
#   while len(A)!=0 and len(B)!=0:
#     if A[0]<=B[0]:
#       result.append(A.pop(0))
#     else:
#       result.append(B.pop(0))
#   result.extend(A)
#   result.extend(B)
#   return result
# def mergesort(A):
#   if len(A)<2:
#     return A 
#   mid=len(A)//2
#   left=mergesort(A[:mid])
#   right=mergesort(A[mid:])
#   return merge(left,right)
# n=int(input())
# a=list(map(int,input().split()))
# print(' '.join(map(str,mergesort(a))))
