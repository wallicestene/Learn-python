# advance OOP concept in python
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_age(self, age):
#         self.age = age
#     def set_name(self, name):
#         self.name = name

# d = Dog("Paker",12)
# print(d.get_name())
# # print(d.get_age())
# d.set_age(23)
# print(d.get_age())


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade  # 0 - 100

#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_students(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)


# s1 = Student("max", 19, 87)
# s2 = Student("Ali", 20, 95)
# s3 = Student("Emma", 17, 78)

# c1 = Course("Biology", 2)
# c1.add_students(s1)
# c1.add_students(s2)
# print(c1.add_students(s3))

# print(c1.get_average_grade())
# print(c1.students[0].name)


# inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"\n my {self.age} year old {self.name} is walking down the street.\n")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


# my_cat = Cat("Kit", 3, "black")
# # my_cat.speak()
# print(my_cat.name)
# print(my_cat.color)
# my_cat.walk()


# my_dog = Dog("Rex", 4)
# my_dog.walk()
# my_dog.speak()


# Class attributes and methods
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # class methods
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


# p1 = Person("John")
# # print(p1.number_of_people)
# p2 = Person("John")
# # print(p2.number_of_people)

# # accessing class methods
# print(Person.get_number_of_people())


# static methods
class Math:
    @staticmethod #do not have access to an instance
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("running")
# accessing static methods
# print(Math.add5(5))
# print(Math.add10(5))
# Math.pr()
        
