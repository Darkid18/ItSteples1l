# try:
#     print("negrik123")
#     print(10/0)
#     print("Litvin")
# except (NameError, ZeroDivisionError):
#     print("STUPID ERROR")
# else:
#     print("You have been smart for a few seconds!")
# finally:
#     print("You stupid?")
#
#
# print('Work')
#
# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"{type(var_1)}, YOU NEED USE STRING!")
#     else:
#         print(var_1)
#
#
# num = "123"
# checker(num)
#
# class BuildingError(Exception):
#     def __str__(self):
#         return f"BuildingError"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         print("Enough material")
#     else:
#         raise BuildingError(amount_of_material)
#
# materials = 1233
# check_material(materials, 300)



# try:
#     numerator = int(input("Enter a number: "))
#     denominator = int(input("Enter a number: "))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("Enter a valid number")

# words = ["Apple", "banan", "pineapple"]
# try:
#     index = int(input("Enter a number: "))
#     word = words[index]
#     print\
#



#
# import warnings
#
# warnings.simplefilter("ignore", ImportWarning)
# warnings.simplefilter("always", SyntaxWarning)
#
# warnings.warn("Warning, no code there", SyntaxWarning)
# warnings.warn("Warning 2, no code there", ImportWarning)





