# price = 1_000_000
# good_credit = False
# if good_credit:
#     print(f"You will need to put down $ {price * 0.1}  ")
# else:
#     print(f"You will need to put down $ {price * 0.2}  ")
# has_high_income = True
# has_criminal_record = True
# has_good_credit = True
# logical "and(both should be true)" and "or(at least one should be true)" and  "not" operator

# if has_high_income and has_good_credit :
#     print("you are eligible for loan")
# else:
#     print ("sorry you cannot get a loan")

# if has_high_income and not has_criminal_record :
#     print('You can apply for the loan')
# else:
#     print("not eligible for loan")

# temperature = 15
# if temperature >= 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither hot nor cold")

# name = "wall"
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")
# while loop using a guessing game
# secret_number = 9

# # guess_count = 0
# # guess_limit = 3

# # while guess_count < guess_limit:
# #     guess = int(input("Guess "))
# #     guess_count += 1
# #     if guess == secret_number:
# #         print("you win")
# #         break
# # else:
# # print("you lose")


# a car game to master the while loop
# command = ""
# started = False
# while True:
#    command = input("> ").lower()
#    if command == "help":
#      print('''
#      start - to start the car
#      stop - to stop the car
#      quit - to exit''')
#    elif command == "start":
#       if started:
#         print("The car already started, what are you doing! 😒")
#       else:
#         started = True
#         print("The car started")
#    elif command == "stop":
#       if not started:
#         print ("the car has already stopped.")
#       else:
#          started = False
#          print("The car stopped")

#    elif command == "quit":
#     break
#    else:
#     print("i dont understand that")

# for loops

# prices = [10, 20, 30, 40, 50]
# total = 0
# for i in prices:
#     total += i
# print(f"total is {total}")

# for i in range(4):
#     for j in range(3):
#         print(f"({i}, {j})")


# list = [2,2,2,2,6]
# for item in list:
#     output = ""
#     for i in range(item):
#         output += "X"
#     print(output)

# list = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
# for day in list:
#     if day == "wed":
#         continue
#     print(day)
# numbers = [1,6,2,8,3,4,5,7]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# # remove dublicates
list1 = [1, 2, 2, 3, 4, 4, 6, 7, 7]
list2 = [
    1,
    3,
    4,
    14,
    15,
    10,
    7,
    8,
]
# print(list(set(list1).intersection(list2))) # elements the both lists share
# print(list(set(list1).difference(list2))) #elements in list1 but not in list2
# print(list(set(list2).difference(list1))) # elements in list2 but not in list1
# print(list(set(list1).union(list2)))# elements in in both lists1 and list2
# print(list(set(list1)))
# print(list(set(list1).symmetric_difference(list2)))# elements in in both lists1 and list2 or only in one of them

# list = [1,2,2,3,4,4,6,7,7]
# uniques = []
# for i in list:
#     if i not in uniques:
#         uniques.append(i)
# print(uniques)

# Dictionaries in python just like objects in javascript

customer = {"name": "John Smith", "age": "30", "is_verified": True}
customer["gender"] = "male"  # adds the key gender and assigns it the value male
# print(customer.get("gender"))
# print(customer.get("DOB", "24-04-2002")) # if the key is not available it creates it
# customer["name"] = "Waweru" #assigns the key a new value
# customer["email"] = "waweru@gmail.com"
# print(customer.get("DOB", "24-04-2002"))
# print(customer.get("DOB")) # will return none cause there is no key


# numbers = {
#     1: "one",
#     2: "two",
#     3: "three",
# }
# phone = (input("enter phone number "))
# for i in phone:
#     print(numbers[int(i)])
#     or use the get method
#     print(numbers.get(characters))

# # emoji converter


# def get_Emoji(userInput):
#     words = userInput.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "😔",
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word)+ " "
#     print(output)

# get_Emoji(input("> "))


# error handling
# try:
# except:

# def check_palindrome(word):
#     reversed_word = word[::-1]
#     if reversed_word == word:
#         return True
#     else:
#         return False


# print(check_palindrome("racecar"))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def talk(self):
#         print("I'am talking")

# myPoint = Point(2,3)
# print(myPoint.x)
# print(myPoint.x)
# print(myPoint.talk())

# # classes in python || OOP concept in python
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def talk(self):
#         print(f"{self.name} is talking!")

# person1 = Person("John")
# person2 = Person("Jane")
# # print(person1.name)
# person2.talk()
# person1.talk()


# # Inheritance in Python(OOP concept)

# class Mammal:
#     def walk(self):
#         print("Walking")

# class Dog(Mammal):
#     def bark(self):
#         print("Dog is barking")
# class Cat(Mammal):
#     def jump(self):
#         print("cat is jumping")


# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.jump()
# cat1.walk()
# dog1 = Dog()
# dog1.walk()
# dog1.bark()

# cat1 = Cat()
# cat1.walk()
# cat1.anoying()

# OOP
# class TikTok:
#     def __init__(self):
#         self.name = ""
#         self.followers = 0
#         self.bio = ""
#     def set_name(self,name):
#         self.name = name
#     def get_name(self):
#         return f"Hello my name is {self.name}".title()
#     def add_follower(self):
#         self.followers += 1
#     def remove_follower(self):
#         self.followers -= 1
#     def get_followers(self):
#         return f"M have {self.followers} followers".title()
#     def set_bio(self, bio):
#         self.bio = bio
#     def get_bio(self):
#         return f"My biography: {self.bio}".title()


# my_tiktok = TikTok()
# my_tiktok.set_name("Wallace Waweru")
# print(my_tiktok.get_name())
# my_tiktok.add_follower()
# my_tiktok.add_follower()
# my_tiktok.add_follower()
# my_tiktok.add_follower()
# my_tiktok.remove_follower()
# print(my_tiktok.get_followers())
# my_tiktok.set_bio("Im a software developer.")
# print(my_tiktok.get_bio())

# importing modules

# import converters # imports the whole module

# print(converters.kg_to_lbs(56))
# print(converters.lbs_to_kg(34))
# print(converters.number)
# from converters import (
#     kg_to_lbs,
#     lbs_to_kg,
#     number,
# )  # import specific functions from the modules

# print(kg_to_lbs(13))
# print(lbs_to_kg(30))
# print(number)
import converters as con  # this is like renaming the module name to what you want to use

# print(con.number)
import utils

# print(utils.get_max([1,2,3,4,5,6,7]))
from utils import get_max_num

# print(get_max_num([1,2,3,4,5,]))

import ecommerce.shipping

# ecommerce.shipping.calc_shipping()

import ecommerce.shipping as ecommerce_shipping

# ecommerce_shipping.calc_shipping()
from ecommerce.shipping import calc_shipping as shipping

# shipping()

# generate random numbers
import random

# for i in range(5):
#     print(random.randint(0, 10))

list = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
# print(random.choices(list, k=3)) # gives out three choices from the list randomly
# print(random.choice(list)) # gives out one choice from the list randomly

import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.digits)
# print(string.printable)


# class Dice:
#     def __init__(self):
#         pass

#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second

# dice = Dice()
# print(dice.roll())

from pathlib import Path

path = Path()
# print(path.mkdir()) # creating a directory

# print(path.rmdir()) # removing a directory

# for file in path.glob("*.py"): # all .py files in the current directory
#     print(file)


# how to make a directory
# def create_directory():
#         try:
#             folder_name = input("Enter directory name: ")
#             path.joinpath(folder_name).mkdir()
#             print("directory successfully created")
#         except Exception as e:
#             print("error creating directory", str(e))
# create_directory()
# def remove_directory():
#     try:
#           folder_name = input("enter folder name: ")
#           path.joinpath(folder_name).rmdir()
#           print("Folder Successfully Deleted!")
#     except Exception as e:
#          print ("Error deleting the folder.\n",str(e))
# remove_directory()
# how to check if a directory already exists

# while True:
#     buyingPrice = int(input("Enter Buying price: "))
#     sellingPrice = int(input("Enter selling price: "))

#     # print("\nProfit is : ", profit )
#     if sellingPrice > buyingPrice:
#         profit = (sellingPrice - buyingPrice)
#         print(f"You made a profit 💪 of: {profit}" )
#     else:
#         loss = buyingPrice - sellingPrice
#         print(f"You made a Loss of 😔: {loss}")

# list comprehension
# print([x *2 for x in range(10)])
# list1 = [1,2,3,4,5]
# filter_list = filter(lambda number: number > 2, list1)
# print(list(filter_list))

# print(sum(list1))
# print(max(list1))
# print(min(list1))
# map_list = map(lambda item: item **2, list1) #map method
# print(list(map_list))

# fetching data in python
import requests

response = requests.get("https://blog-mgrd.onrender.com/")
data = response.json()
for post in data:
    if post["_id"] == "66391a88898ba8400d89b9b6":
        print(post["title"])


def covert_to_snake_case(camel_case_string):
    # using list comprehension
    converted_to_snake_case = [
        "_" + character.lower() if character.isupper() else character
        for character in camel_case_string
    ]
    return "".join(converted_to_snake_case).strip("_")
    # using for loop
    # converted_to_snake_case = ""
    # for character in camel_case_string:
    #     if character.isupper():
    #         converted_to_snake_case += "_" + character.lower()
    #     else:
    #         converted_to_snake_case += character
    # clean_converted_snake_case = converted_to_snake_case.strip("_")
    # return converted_to_snake_case


def main():
    print(covert_to_snake_case("IAmAPascalCasedString"))


# if __name__ == "__main__":
#     # main()
