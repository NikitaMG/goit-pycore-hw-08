import math
from random import random

import pip

# def check(x):
#     if x < 0:
#         return "minus"
#     elif x > 0:
#         return "plus"
#     else:
#         return "zero"
# def analize(y):
#     if y % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# result = analize(5)
# print(result)
# result = []
# odd = []
#
#
# def check(nums):
#     for num in nums:
#         if num % 2 == 0:
#             result.append(num)
#         else:
#             odd.append(num)
#             num += 1
#
#
# check([1, 2, 3, 4, 5, 6])
# print(result)
# print(odd)
# def count_vowel(text):
#     vowel = "aeiouAEIOU"
#     count = 0
#     for i in text:
#         if i in vowel:
#             count+=1
#     return count
#
# print(count_vowel("hello world"))


# lst = [1, 2, 2, 3, 4, 4, 5]
#
# def remove_el (lst):
#     return list(set(lst))
#
# print(remove_el(lst))

# list = [80, 45, 67, 90, 30, 55, 100]
# marks = {}
# marks["average"] = sum(list) / len(list)
# marks["high"] = max(list)
# marks["lowest"] = min(list)
# def calculate(lst,dict):
#     marks_count =sum(1 for i in lst if i >= 50)
#     dict["passed"] = marks_count
#
# calculate(list, marks)
#
# print(marks)
#
# library = {
#             "1984": {"author": "Orwel", "year": 1991},
#            "nemo": {"author": "john", "year": 2000}
#            }
# library["1984"]["genre"] = "classic"
# library["nemo"]["genre"] = "fiction"
#
# del library["1984"]
# library["holmes"] = {"author": "skot", "year": 1985, "genre": "detective"}
#
# for title,details in library.items():
#     print(f"Title: {title}")
#     for key, value in details.items():
#         print(f"{key.capitalize()}: {value}")
# # print(library["nemo"]["genre"])

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)
#
# odd = [i for i in range(1,16) if i % 2 != 0 ]
# print(odd)
#
# dict = {i: i ** 2 for i in range (1,6)}
# print(dict)

# def multiply(a, b):
#     return a * b
# print(multiply(2,4))
#
# multiply2 = lambda a,b: a * b
# print(multiply2(2,4))


# while True:
#     try:
#         ask = int(input("write a number"))
#         result = 100 // ask
#     except ValueError:
#         print("it is not a number")
#         continue
#     except ZeroDivisionError:
#         print("can`t divide by 0")
#         continue
#     else:
#         print(f"{result}")
#         break
# def longest_word(sentence: str) -> str:
#
#     words = sentence.split()
#     letters = max(len(word) for word in words)
#
#     for word in words:
#         if len(word) == letters:
#             return word
# def longest_word(sentence: str) -> str:
#     words = sentence.split()  # Разбиваем строку на слова
#     longest = ""  # Переменная для хранения самого длинного слова
#
#     for word in words:
#         if len(word) > len(longest):  # Если текущее слово длиннее
#             longest = word  # Обновляем переменную
#
#     return longest  # Возвращаем самое длинное слово
#
# # Тесты
# print(longest_word("I love programming"))  # "programming"
# print(longest_word("Python is awesome"))  # "awesome"
# print(longest_word("one two three four five"))  # "three"
# print(longest_word("Hello world"))  # "Hello"

# def first_word(text: str) -> str:
#     text = text.lstrip(" .,!?:")  # Убираем знаки препинания в начале
#     words = text.split()  # Разбиваем строку на слова
#     return words[0].strip(".,!?")  # Убираем знаки в конце первого слова
#
#
# print("Example:")
# print(first_word("Hello world"))
#
# # These "asserts" are used for self-checking
# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
# assert first_word("greetings, friends") == "greetings"
# assert first_word("... and so on ...") == "and"
# assert first_word("hi") == "hi"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

# with open("myfile", "w") as f:
#     f.write("Hello, Python!\n")
# with open("myfile","a") as f:
#     f.write("Let's learn file handling!")
#
# with open("myfile", "r") as f:
#     for line in f:
#         print(line)

# s = "hello mama"
# y = list(s)
# for i in y:
#     if y[0] == "h":
#         print("okey")
#         break
#     else:
#         print("not")
#         break
# import random
# number = random.randint(1,100)
# print(number)
#
# from my_module import calc as plus, sub as minus,multi as times,devision as div
# print(plus(10,5))
# print(minus(10,5))
# print(times(10,5))
# print(div(10,5))

# numbers = [i**2 for i in range(1,11)] Эта строка преобразует число num в список его цифр.
# # print(numbers)

# def plusOne(digits):
#      x = int("".join(map(str,digits)))
#      x += 1
#      return [int(digit) for digit in str(x)]
# print(plusOne([9]))
# import math
# x = 14
# y = math.sqrt(x)
# if y == round(y):
#     print("Okay")
# else:
#     print("no")

# x = 0
# y= list(map(int, str(x)))
# nums = sum(y)
# if nums>10:
#     print(sum(list(map(int, str(nums)))))
# else:
#     print(nums)

# def isPerfectSquare(num):
#     result = num ** 0.5
#     if result == round(result):
#         return True
#     else:
#         return False
#
# def addDigits(num):
#     while num >=10:
#         num = sum(list(map(int, str(num))))
#     return num
# print(addDigits(199))
#
# n = 14
# if n == (2*3) or n == (2*5) or n == (3*5):
#     print("yes")
# else:
#     print("no")
#
# def isUgly(n):
#     for num in [2,3,5]:
#         while n % num == 0:
#             n //=num
#     return n == 1
# print(isUgly(6))

# def fib(n):
#     if n == 1:
#         return 1
#     elif n <= 0:
#         return 0
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(3))


# def fib(self, n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(3)) - fibonachi number
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# count = 0
# i = 0
# while i < len(nums):
#     if nums[i] == val:
#         nums.pop(i)
#         count += 1
#     else:
#         i+=1
#     nums.sort()
# print(nums)
# print(count)

# nums = [0,0,1,1,1,2,2,3,3,4]
# numset=set(nums)
# numlist = list(numset)
# print(numlist)


# def removeDuplicates(nums):
#     x = 0
#     y = set()
#     for i in nums:
#         if i not in y:
#             nums[x] = i
#             y.add(i)
#             x+=1
#     return y
# print(removeDuplicates([1, 1, 2, 2, 3]))


# def maxProfit(prices):
#     min_price = float("inf")
#     max_profit = 0
#
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#
#     return max_profit
#
# # Тест
# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([7,6,4,3,1]))
# nums = [1,1,2,2,3]
# nums2=[]
# for i in nums:
#     if not i in nums2:
#         nums.remove(i)
#         nums2.append(i)
#     if not i in nums and nums2:
#         print(i)
# listik = [2,5,8,9,10]
# lst = [i+1 for i in listik]
# print(lst)

# text = "Hello my Name is Nikita and I love study Python"
# ch = input("chose the ch: ")
# count = 0
# for i in text:
#     if i == ch:
#         count+=1
# print(count / len(text) * 100)

# class Vehicle:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         return (self.brand, self.model, self.year)
#
# class Car(Vehicle):
#     def __init__(self, brand, model, year,fuel_type):
#         super().__init__(brand, model, year)
#         self.fuel_type = fuel_type
#
#     def display_info(self):
#         return (self.brand, self.model, self.year,self.fuel_type)
#
#
# car = Car("BMW","X5",2015,95)
# print(car.display_info())

import datetime


def get_days_from_today(date):
    try:
        user_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        current = datetime.date.today()
        delta = current - user_date
        return delta.days
    except ValueError:
        return "Формат дати введено неправильно! Правильний формат: 'РРРР-ММ-ДД'. "


print(get_days_from_today('2025-05-10'))
