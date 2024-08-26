"""bubble sort"""
a=[5,7,3,5,1,8,6]
k=0

while k<len(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            x=a[i+1]
            a[i+1]=a[i]
            a[i]=x

    k+=1
print(a)
