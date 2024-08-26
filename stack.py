class Stack:
    def __init__(self):
        self.item = []


    def push(self, item):

        self.item.append(item)

    def pop(self):

        if not self.is_empty():
            return self.item.pop()  # Return the removed item
        raise IndexError("Pop from an empty stack")

    def is_empty(self):

        return len(self.item) == 0

    def __str__(self):

        return str(self.item)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
print(s)

""" queue """
class queue:
    def __init__(self):
        self.item = []

    def push(self, item):

        self.item.append(item)

    def pop(self):

        if not self.is_empty():
            return self.item.pop(0)
        raise IndexError("Pop from an empty stack")

    def is_empty(self):

        return len(self.item) == 0

    def __str__(self):

        return str(self.item)


q = queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.pop()
print(q)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # l=[1,2,3,4,5]
# # # # # a=[]
# # # # # i=len(l)
# # # # # j=i
# # # # # k=0
# # # # # print()
# # # # # while k<j:
# # # # #
# # # # #             a.append(l[-1])
# # # # #             l.pop()
# # # # #             k+=1
# # # # # print(a)
# # # # # print()
# # # # # l=[1,2,3,4,5]
# # # # # j=len(l)
# # # # # a=[]
# # # # # k=0
# # # # # while k<j:
# # # # #         a.append(l[-1])
# # # # #         l.pop()
# # # # #         k+=1
# # # # # print(a)
# # # # # print()
# # # # #
# # # # # a=[1,2,3,5]
# # # # # print(a)
# # # # # length=len(a)
# # # # # b=0
# # # # #
# # # # # # for i in a:
# # # # # #     if a[-1]:
# # # # # #         print(a[-1])
# # # # # #     if a[i]==a[i]+1:
# # # # # #         pass
# # # # # #     else:
# # # # # #         print(a[i]+1)
# # # # #
# # # # #
# # # # # a='hello World'
# # # # # b=''
# # # # # for i in a:
# # # # #     b=i+b
# # # # # print(b)
# # # # # print()
# # # # # def reverse_string(s):
# # # # #     return s[::-1]
# # # # #
# # # # # print(reverse_string("hello world"))  # Output: "olleh"
# # # # #
# # # # #
# # # # #
# # # # # #1 2 3 4 5
# # # # l=[5,6,7,9]
# # # # n=sum(l)+5
# # # # total = n*(n+1)//2
# # # # print(total)
# # # # print(sum(l))
# # # # t=sum(l)-total
# # # # print(t)
# # # #
# # # import matplotlib.pyplot as plt
# # #
# # # # Data
# # # x = [1, 2, 3, 4, 5]
# # # y = [2, 4, 6, 8, 10]
# # #
# # # # Creating a line plot
# # # plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = 2x')
# # #
# # # # Adding titles and labels
# # # plt.title('Simple Line Plot')
# # # plt.xlabel('X-axis')
# # # plt.ylabel('Y-axis')
# # #
# # # # Adding a legend
# # # plt.legend()
# # #
# # # # Display the plot
# # # plt.show()
# # #
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # #
# # # Sample data
# # tips = sns.load_dataset('tips')
# #
# # # Creating a scatter plot with a regression line
# # sns.lmplot(x='total_bill', y='tip', data=tips, height=6, aspect=1.5)
# #
# # # Adding titles and labels
# # plt.title('Scatter Plot with Regression Line')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Tip')
# #
# # # Display the plot
# # plt.show()
# # # Creating a histogram
# # sns.histplot(tips['total_bill'], kde=True, color='m')
# #
# # # Adding titles and labels
# # plt.title('Histogram of Total Bill')
# # plt.xlabel('Total Bill')
# # plt.ylabel('Frequency')
# #
# # # Display the plot
# # plt.show()
# # # Data
# # x = [1, 2, 3, 4, 5]
# # y1 = [1, 4, 9, 16, 25]
# # y2 = [2, 3, 4, 5, 6]
# #
# # # Creating a figure with subplots
# # plt.figure(figsize=(10, 5))
# #
# # # Plot 1
# # plt.subplot(1, 2, 1)
# # plt.plot(x, y1, 'r--', label='y = x^2')
# # plt.title('Quadratic')
# # plt.xlabel('X-axis')
# # plt.ylabel('Y1-axis')
# # plt.legend()
# #
# # # Plot 2
# # plt.subplot(1, 2, 2)
# # plt.plot(x, y2, 'g-', label='y = x + 1')
# # plt.title('Linear')
# # plt.xlabel('X-axis')
# # plt.ylabel('Y2-axis')
# # plt.legend()
# #
# # # Adjust layout to prevent overlap
# # plt.tight_layout()
# #
# # # Display the plots
# # plt.show()
# #
# # import plotly.express as px
# #
# # # Sample data
# # df = px.data.iris()
# #
# # # Creating a scatter plot
# # fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', size='petal_length', hover_data=['petal_width'])
# #
# # # Display the plot
# # fig.show()
# import pandas as pd
# data={
#     'name':['umar','ziya','bihu'],
#     'id':[1,2,3]
# }
# data=pd.DataFrame(data)
# print(data)