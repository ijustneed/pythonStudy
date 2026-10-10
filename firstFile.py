import numpy as py
# 快捷键ctr+/

# 变量定义 变量 = 值
num=1.1
print(num)
print(int(num))
name='mike'
age=20
print(f'{name} is {age} years old')
#input
# sname=input("enter your name")
# age=input("enter your age")
# print(f'{sname} is {age} years old')
if age>=20 and name=='mike':
    print('It\'s you')
#match like java:switch
day=1
match day:
    case 1:print(day)
    case 2:print(day)
    case 3:print(day)
    case _:print("nothing")
#list
dataList=[1,2,3,4,5,6]
for i in range(len(dataList)-1,-1,-1):
    print(dataList)
    del dataList[i]

# print(dataList[0])
#最后一个是-1 切片0:5 不包括最后一个元素 append()加元素 del删元素
# print(dataList[-2])
# dataList.append(7)
# print(dataList)
# del dataList[0]
# print(dataList)
#tuple元组 与list类似 但是元素不能修改 并且用中括号
tup1=("a","b","c")
#两个元组可以拼接 不能删除其中的元素 可以整个删除
#字典 类似java的hashmap key-value
studentList={'name':'mike','age':20,'city':'york'}
print(studentList['name'])

num_list=[19,23,54,64,87,20,109,232]
num_list1=[]
for num in num_list:
    if num%2==0:
        num_list1.append(num*num)

print(num_list1)