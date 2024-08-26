# l=[1,2,3,4,5,6,7]
# m=[]
# length=len(l)
# k=3
# for i in range(k,len(l)):
#
#         m.append(l[i])
# for i in range(0,k):
#     m.append(l[i])
#
# print(m)
#
#
#
# a=[1,2,3]
# b=3
# a.append(b)
# print(a)
# arr=[1,2,4,5]
#
# def b(arr):
#     a=1
#     for i in range(len(arr)):
#         if a == arr[i]:
#             a += 1
#         else:
#             return a
#     return a
# arr=[1,2,4,5]
# # print(b(arr))
#
# class Solution:
#     arr=[1,2,3,5]
#     # Note that the size of the array is n-1
#     def missingNumber(self, n, arr):
#
#         # code here
#         # a = 1
#         # for i in range(len(arr)):
#         #     if a == arr[i]:
#         #         a += 1
#         #     else:
#         #         return a
#
#         expected_sum = n * (n + 1) // 2
#         actual_sum=sum(arr)
#         missing_np=expected_sum-actual_sum
#         return missing_np
#
#
# arr=[6,6,2]
# a=Solution()
# print(a.missingNumber(5,arr))
#
#
# class Solution:
#     def duplicates(self,arr,n):
#         a=[]
#         a=arr
#
#         # code here
#         for i in range(n):
#             if arr[i] in a:
#                 a.append(arr[i])
#             else:
#                 continue
#         return a
#
#
#
#
#
# # s=Solution()
# # arr=[1,2,2]
# # print(s.duplicates(arr,3))
#
# a = 0
# b = 1
# x=int(input("enter a num: "))
# print(a)
# print(b)
#
# i = 0
# while i < x-2:
#
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     i+=1
# print()
#
# """0 1 1 2 3 5 8"""
#
# for i in range(0,5):
#     print(i)
#
#
# class stack:
#     def __init__(self):
#         self.a=[]
#     def push(self,num):
#         self.a.append(num)
#         return self.a
#     def pop(self):
#         if self.a:
#             return "list is empty"
#         else:
#             self.a.pop()
#
#             return self.a
#     def is_empty(self):
#         return len(self.a)==0
#
#     def __str__(self):
#
#         return str(self.a)
#
# s=stack()
# s.push(1)
# s.pop()
# s.push(2)
# s.pop()
# s.push(2)
# s.push(2)
# s.push(2)
# s.push(2)
# s.pop()
# s.pop()
# print(s)
#
#
#
# """2,5,7,5,2"""
# a=[2,1,7,3]
# k=0
# x=0
# length=len(a)
# while k<length:
#     for i in range(len(a)-1):
#         if a[i]>a[i+1]:
#             x=a[i+1]
#             a[i+1]=a[i]
#             a[i]=x
#         else:
#             pass
#     k+=1
#
# print(a)
#
#
#
# a = [2, 1, 7, 3]  # List to be sorted
# k = 0
# length = len(a)
#
# # Bubble Sort implementation
# while k < length:
#     for i in range(len(a) - 1):
#         if a[i] > a[i + 1]:  # Compare adjacent elements
#             # Swap elements if they are in the wrong order
#             x = a[i + 1]
#             a[i + 1] = a[i]
#             a[i] = x
#     k += 1  # Move to the next pass
#
# print("Sorted list:", a)
#
#
# def sort(num):
#     for i in range(0,len(num-1)):
#         for j in range(i):
#             if num[j]>num[j+1]:
#                 temp=num[j]
#
# a=[5,4,3,7,1]
# for i in range(len(a)):
#
#     print(a[i])
#     print()
# print(len(a))
#
#
# a=[1,2,3,4,5,6,7,8]
# x=3
# a=0
# while a==x:
#         for i in range(len(a)):
#             if a[i]==x:
#                 print()
#
#
#
#
# class Solution:
#     def duplicates(self,a):
#         c=[]
#         for i in range(len(a)):
#             for j in range(i):
#                 if a[i]==a[j]:
#                     c.append(a[i])
#         result = ' '.join(map(str, c))
#         if len(c)==0:
#             return -1
#         else:
#             return result
#
#
#
#
# a=[3,3,5,5,6,4,7]
# s=Solution()
# print(s.duplicates((a)))
#
#
#
#
# arr=[3,3,5,5,6,4,7]
#
# print(arr)
# s=[]
# for i in range(len(arr)-1):
#     if arr[i]==arr[i+1]:
#         s.append(arr[i])
#
# print(s)
#
#
# a=[5,4,6,8,3,2,1,9,7]
# k=0
# for i in range(len(a)):
#     for j in range(i):
#         if a[i]<a[j]:
#             k=a[i]
#             a[i]=a[j]
#             a[j]=k
# print(a)
#
# a=[5,4,6,8,3,2,1,9,7]
# for i in range(len(a)):
#     min=i
#     for j in range(min+1,len(a)):
#         if a[j]<a[min]:
#             min=j
#
# arr=[1,2,3,4,5,6,7,8]
# a=arr[4:]+arr[0:4]
# print(a)
#
# s=5
# for i in range(len(a)):
#     if a[s]<i:
#         print(a[i],end=' ')
#
import pandas as pd
data={
    "id":[1,2,3,4,5,6,7,8,9,10,11],
    "name":["umar","ziya","bichu","aqsa",'misba','maaz','rida','safa','hiza','saad','zaid'],
    "city":["pune","kudchi","mumbai","belgam",'belgam','belgam',"kudchi","kudchi","kudchi","mumbai","mumbai"]
}
d=pd.DataFrame(data)
print(d)
# print(d)
# print()
# print(d.tail(5))
# print(d.columns)
# print(d[['name','city']][0:5])
#
# print(d.loc[0:5])
# print(d.iloc[2,1])
#
# print(d.loc[d['city']=='pune'])



