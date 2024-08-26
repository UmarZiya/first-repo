class selection:
    def sort(self,arr):
        for i in range(len(arr)):
            min=i
            for j in range(i+1,len(arr)):
                if arr[min]>arr[j]:
                    min = j
                arr[i], arr[min] = arr[min], arr[i]
        print(arr)


a="world"
b="hello"
a,b=b,a
print(a +' '+b)
s=selection()
arr=[4,3,5,7,9,2]




