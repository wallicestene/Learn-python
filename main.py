# def get_name(age):
#     if age < 5 :
#         print("you are still a baby")
#     elif age == 5 :
#         print("Enjoy your kindergarten")
#     else:
#         print("You are a grown up now")
# age = int(input("Enter your age: "))
# get_name(age)


# # for loop

import math

# list1 = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
# for day in list1:
#     if day == "thur":
#         # continue
#         break
#     print(day)
# print("pi is :", math.pi)

# while loop
# i = 1
# while i  < 10:
#     print(i * "*")
#     i = i + 1
# red_bucket = "wallace"
# print ("The red bucket is " + str(red_bucket))

# def add_ten_to_age(age):
#     newAge = age + 10
#     return newAge
# print(add_ten_to_age(10))

# string methods in python

# name = "wallace waweru"
# print("wallace" in name)
# print("waweru" not in name)
# print(name.upper())
# print(name.title())
# # print(name.lower())
# print(name[:])
# print(name[1:-1])

# formatted strings
# first = "wallace"
# second = "Waweru"

# message = first + " " "[" + second + "]" + " is a coder"
# msg = f"{first} [{second}] is a coder"
# print(message)

# course = "python for beginners"
# print(len(course))
# print(course.replace("python", "javascript"))
# print(course.replace("python", "Javascript"))
# print(course.replace("beginners", "absolute beginners"))
# print("python" in course)
# print(course.title())


# function to add all even numbers in a array
# def getEven(nums):
#     even_numbers = []
#     total = 0
#     for num in nums:
#         if num % 2 == 0:
#             even_numbers.append(num)
#             total += num
#     return f"even numbers {even_numbers} and total {total}"


# print(getEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# x = (10 + 3) * 2
# print(x)
# price = 5
# print( not price < 10)

# if Statements
# weight = input("weight: ")
# unit = input("(K)g or (L)bs: ")
# if unit == "k" or unit == "K" :
#     print("Weight in lbs: ",(float(weight) * 2.20462).__round__(3))
# else:
#     print("Weight in kg: ",(int(weight)/2.20462).__round__(3))

# while loop
# i = 1
# while(i <= 10):
#     print(i * 2 )
#     i = i + 1

# Lists in python

names = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
# print(names[1:2])
# print(names.index("tue"))
# print(names.pop())
# print(names.remove("tue"))
# print(names.insert(1, "tuesday"))
# print(names.copy())
# names.extend([12,34])
# names.append("jan")
# print(names)

# list methods

numbers = [1, 2, 3, 4, 5]
# numbers.append(6) # add element at the end of the list
# numbers.pop() # remove the last elelment or whatever index you put
# numbers.insert(6,4) # add an element on a specific place on the list
# numbers.remove(3) remove a specific element from the list
# numbers.clear() # remove all elements from the list
# print(len(numbers))

# for loops
# for number in range(1,10+1):
#     print(number)

# for item in numbers:
#     print(item)

# i = 0
# while i <= len(numbers):
#     print(i)
#     i += 1
# the range function in python

# for i in range(0, 10, 2):
#     print(i)

# tuples in python
# they are immutable
def lastWord(s):
    words = s.split()
    last_word = words[-1]
    print(len(last_word))

lastWord("Hello World")  # should return 5


numbers = (1, 2, 3)
# print(numbers.count(2))
# print(numbers.index(3))


# sentence = str(input("enter sentence: "))
# print(sentence.title())

# from tkinter import *

# root = Tk()
# root.configure(background='aqua')
# root.title('AREA CALCULATOR')
# root.geometry('500x450')

# class Rectangle:
#     def __init__(self,M):
#         self.text=StringVar()

#         LF=LabelFrame(root, text="Calculations",bg='aqua',relief='solid')
#         LF.pack(expand=None,fill=BOTH,padx=50,pady=50)
#         self.l1=Label(LF,text="Length",bg='aqua')
#         self.l1.grid(row=0,sticky=W)
#         self.L2=Label(LF,text="Width",bg='aqua')
#         self.L2.grid(row=1,sticky=W)
#         self.L3=Label(LF,text="Area",bg='aqua')
#         self.L3.grid(row=2,sticky=W)
#         self.e1=Entry(LF)
#         self.e1.grid(row=0,column=1)
#         self.e2=Entry(LF)
#         self.e2.grid(row=1,column=1)
#         self.e3=Entry(LF,text="",textvariable=self.text)
#         self.e3.grid(row=2,column=1)
#         self.b1=Button(LF,text="Calculate Area",command=self.calc)
#         self.b1.grid(row=3,column=0)
#     def calc(self):
#        Length=int(self.e1.get())
#        Width=int(self.e2.get())
#        area=Length*Width
#        self.text.set(area)

# R = Rectangle(root)
# root.mainloop()
# from tkinter import *

# root = Tk()
# root.configure(background='aqua')
# root.title('AREA CALCULATOR')
# root.geometry('500x450')

# class Rectangle:
#     def __init__(self, M):
#         self.text = StringVar()

#         LF = LabelFrame(root, text="Calculations", bg='aqua', relief='solid')
#         LF.pack(expand=None, fill=BOTH, padx=50,pady=50, )
#         self.l1 = Label(LF, text="Length", bg='aqua')
#         self.l1.grid(row=0, sticky=W)
#         self.L2 = Label(LF, text="Width", bg='aqua')
#         self.L2.grid(row=1, sticky=W)
#         self.L3 = Label(LF, text="Area", bg='aqua')
#         self.L3.grid(row=2, sticky=W)
#         self.e1 = Entry(LF)
#         self.e1.grid(row=0, column=1)
#         self.e2 = Entry(LF)
#         self.e2.grid(row=1, column=1)
#         self.e3 = Entry(LF, text="", textvariable=self.text)
#         self.e3.grid(row=2, column=1)
#         self.b1 = Button(LF, text="Calculate Area", command=self.calc)
#         self.b1.grid(row=3, column=0)

#     def calc(self):
#         Length = int(self.e1.get())
#         Width = int(self.e2.get())
#         area = Length * Width
#         self.text.set(area)

# R = Rectangle(root)
# root.mainloop()

# print("Hello, {}!".format(name))
"""
r - Read - Default value. Opens a file for reading, error if the file does not exist

a - Append - Opens a file for appending, creates the file if it does not exist

w - Write - Opens a file for writing, creates the file if it does not exist

x - Create - Creates the specified file, returns an error if the file exists

t - Text - Default value. Text mode

b - Binary - Binary mode (e.g. images)
"""
# myfile = open("mypy.txt", "x") #creates a new file returns an error if the file exist
# myfile = open("mypy.txt", "r") #creates a new file an error if the file does not exist
# myfile = open("mypy.txt")
# print(myfile.read()) # reading a file
# print(myfile.read(5)) # Reading the first 5 characters of the file
# print(myfile.readline())

# f = open("mypy.txt", "a")
# f.writelines("now i have added more information")
# f.close()

# f = open("mypy.txt", "rt")
# print(f.read())
# f = open("mypy.txt", "w")
# f.write("Now this is the new content")
# f.close()

# f = open("mypy.txt", "r")
# print(f.read())
import os

# os.remove("mypy.txt") # deleting  a file
# file = open("myfile.txt", "x")

number = 3
# print(f"the number {number}")
def solution(n):
    nums_as_string = str(n) 
    sum = 0
    for i in nums_as_string:
        singleNum = int(i)
        sum = sum + singleNum
    return sum
print(solution(12345))  # should return 15

