# 1
# class Student:
#     def __init__(self, name, age, average_score):
#         self.name = name
#         self.age = age
#         self.average_score = average_score
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_average_score(self):
#         return self.average_score
#
#     def set_average_score(self, average_score):
#         self.average_score = average_score
#
#
# student1 = Student('Ваня', 17, 4.1)
# print(student1.get_name())
# print(student1.get_age())
# print(student1.get_average_score())
#
#
# student1.set_name('\n''Глеб')
# student1.set_age(16)
# student1.set_average_score(4.6)
#
#
# print(student1.get_name())
# print(student1.get_age())
# print(student1.get_average_score())




#2
# class Rectangle:
#     def __init__(self, length, width):
#         self.lenght = length
#         self.wight = width
#
#     def get_square(self):
#         return self.lenght * self.wight
#
#     def get_perimeter(self):
#         return 2 * (self.lenght + self.wight)
#
#
# rectangle1 = Rectangle(5,7)
# square = rectangle1.get_square()
# perimeter = rectangle1.get_perimeter()
#
# print('Площядь:', square)
# print('Периметр:', perimeter)




#3
# class Car:
#     def __init__(self, brand, model, year_of_release, mileage):
#         self.brand = brand
#         self.model = model
#         self.year_of_relese = year_of_release
#         self.mileage = mileage
#
#     def set_brand(self,brand):
#         self.brand = brand
#
#     def set_model(self, model):
#         self.model = model
#
#     def set_year_of_release(self, year_of_release):
#         self.year_of_relese = year_of_release
#
#     def set_mileage(self,mileage):
#         self.mileage = mileage
#
#     def get_brand(self):
#         return self.brand
#
#     def get_model(self):
#         return self.model
#
#     def get_year_of_relese(self):
#         return self.year_of_relese
#
#     def get_mileage(self):
#         return self.mileage
#
# car1 = Car('BMW', 'm5', 2020, 123000)
# print(car1.get_brand())
# print(car1.get_model())
# print(car1.get_year_of_relese())
# print(car1.get_mileage(),'\n')
#
# car1.set_brand('Mazda')
# car1.set_model('sx5')
# car1.set_year_of_release(2019)
# car1.set_mileage(13000)
#
# print(car1.get_brand())
# print(car1.get_model())
# print(car1.get_year_of_relese())
# print(car1.get_mileage())




#4
# class BankAccount:
#     def __init__(self, client_name, balance, account):
#         self.client_name = client_name
#         self.balance = balance
#         self.account = account
#
#     def set_client_name(self, client_name):
#         self.client_name = client_name
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, score):
#         self.balance += score
#         print(f'Счет пополнен на сумму {score} рулей . Сейчас на балансе {self.balance} рублей.')
#
#     def deduction(self, score):
#         self.balance -= score
#         print(f'Сумма {score} рублей снята со счета. Теперь на балансе {self.balance} рублей.')
#
#     def get_balance(self):
#         print(f'На балансе клиента: {self.client_name}, {self.balance} рублей.')
#
#
# bank_account1 = BankAccount('Ильназ Сафин', 3000,1500)
# bank_account1.deposit(3000)
# bank_account1.deduction(1500)
# bank_account1.get_balance()



#5
# import math
# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def get_types(self):
#         if self.side1 == self.side2 == self.side3:
#             return 'Равносторонний треугольник'
#         elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
#             return 'Равнобедренный треугольник'
#         else:
#             return 'Разносторонний'
#
#     def get_calculation(self):
#         perimeter = (self.side1 + self.side2 + self.side3) / 2
#         calculation_area = math.sqrt(perimeter * (perimeter - self.side1) * (perimeter - self.side2) * (perimeter - self.side3))
#         return calculation_area
#
# traingel1 = Triangle(3,3, 3)
# print(traingel1.get_types())
# print(traingel1.get_calculation(),'\n')
#
# traingel1 = Triangle(4,4, 7)
# print(traingel1.get_types())
# print(traingel1.get_calculation(),'\n')
#
# traingel1 = Triangle(2,5, 6)
# print(traingel1.get_types())
# print(traingel1.get_calculation())