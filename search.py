
"""Linear Search"""
def linear_search(a,x):
    for i in range(len(a)):
        if a[i]==x:
            return f"Found at {i+1}"
    return "number not found"

a=[5,4,3,7,8,5,12,43,87]
x=int(input("enter a  number: "))
l=linear_search(a,x)
print(l)


"""Binary search"""
def binary_search(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return "number found at "+str(mid+1)
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1

    return "number not found"

l=[1,2,3,4,5,6,7,8]
x=int(input("enter a  number: "))
b=binary_search(l,x)
print(b)
