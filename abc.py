# # a=0
# # b=1
# # print(a)
# # print(b)
# # for i in range(4):
# #     c=a+b
# #     print(c)
# #     a=b
# #     b=c
#
# # print("hello")
# #
# #
# # class abc:
# #
# #
# #
# #     def sum(self,n1,n2):
# #         n3 = n1 + n2
# #         return n3
# #
# #
# # a=abc()
# # print(a.sum(1,5))
# #
# #
# # a=1
# # while a<6:
# #     print(a)
# #     a+=1
#
# # my_list = [1, 2, 4, 5, 6]
# # my_list.insert(2, 3)
# # print(my_list)
# #
# #
# # a=(1,2,3,4)
# # print(a[1:3])
#
# # a=[1,2,3] + [1,1,1]
# # print(a)
# #
# # A = (1, 2, 3, 4, 5)
# # print(A[1:4] )
#
#
# # def print_function(A):
# #     for a in A:
# #         print(a + '1')
# # print_function(['a', 'b', 'c'])
# #
# # L=[1,3,2]
# #
# # print(sorted(L))
#
# # a=5
# # for i in range(a):
# #     for j in range(a+1):
# #
# #         print("*",end="")
# #     print("")
# #
# #
# # for i in range(5):
# #     for j in range(i+1):
# #         print("*",end="")
# #     print()
# #
# # for i in range(5):
# #     for j in range(5):
# #         print("*",end="")
# #     print()
#
# # for i in range(1,4):
# #     for j in range(1,4):
# #         print(j,end="")
# #     print()
# #
# # for i in range(1, 4):
# #     for j in range(1, 4):
# #         print(j, end="")
# #     print()
#
# #
# # for i in range(5):  #i=no of rows
# #     for j in range(i+1):  #no of column
# #         print("*",end="")
# #     print()
# # a=5
# # for i in range(1,a):
# #     print(a)
#
#
#
# # a=input("enter your no ")
# # try:
# #     for i in range(1,10+1):
# #         c=int(a)*int(i)
# #         print(c)
# #         print(f"{a} * {i}={c}")
# # except:
# #     print("input sholud always in integer")
# #
# # print("end")
#
# # try:
# #     a=int(input("enter a no: "))
# #     b=int(input("enter a no: "))
# #     c=a*b
# #     print(c)
# #     z=int(input("enter no: " ))
# #
# # except RuntimeError as r:
# #     print("run time error")
# # # except Exception:
# # #     print("pagal no dal ")
# # except ValueError as a:
# #     print("idioy  no dal")
# # except Exception as b:
# #     print("cat  no dal")
# # finally:
# #     print("end")
# from threading import *
# from time import *
# class A(Thread):
#     def run(self):
#         for i in range(10):
#             print("hello")
#             sleep(1)
# #
#
# class B(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hii")
#             sleep(1)
#     def walk(self):
#         for i in range(5):
#             print(i)
#             sleep(1)
#
# a=A()
# b=B()
# a.start()
# b.start()
#
# a=float(input("enter a no: "))
# c=a*20
# print(c)


# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#
#     def add(self):
#         self.c=self.a+self.b
#         return self.c
# a=A(2,4)
# print()add(a.add())
# print("hello")
# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr)

import numpy
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=len(word1)
        j=len(word2)
        a=0
        b=0
        result=[]
        while a<i or b<j:
            if a<i:
                result+=word1[a]
                a+=1

                result+=word2[b]
                b+=1
        return "".join(result)



# s=Solution()
# print(s.mergeAlternately("abc","dsvsd"))


# a="abcd"
# result=''
# for i in a:
#     result=i+result
# print(result)


import numpy as np
import pandas as pd
a=np.array([1,2,3])
print(a)

dict={"a":1,
      "b":2,
      "c":3}
print(dict["a"])
dict["d"]=4
for i in dict:
    print(i,dict[i])

