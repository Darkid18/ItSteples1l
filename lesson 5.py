# def function():
#     pass
#
# class Human:
#     def __init__(self, age = '11', height = 'yes', name = "Vlad"):
#         self.age = age
#         self.height = height
#         self.name = name
#         self.secondname = "Ivan"
#
# sig = inspect.signature(Human)
#
# for param in sig.parameters.values():
#     print(param.name, param.default)
#
#
# rq = inspect
# first_f = function
# nick = Human

# print(inspect.__name__)
# print(rq.__name__)
#
# print(function.__name__)
# print(first_f.__name__)
#
# print(Human.__name__)
# print(nick.__name__)
#
# print(__name__)

# number = 10
# string = "Hello world"

# print(type(first_f))
# print(type(number))
# print(type(string))
#
# print(dir(string))
# print(dir(inspect))

# data = "text"
#
# print(hasattr(data, 'reverse'))
# print(hasattr(data, 'index'))
# print(hasattr(data, 'startswith'))
#
# print(getattr(data, 'startswith', None))
# print(getattr(data, 'reverse', None))

# print(callable(data))
# print(callable(function))

# class First_class:
#     pass
#
# class Second_class(First_class):
#     pass
#
# obj_from_class_2 = Second_class()

# print(issubclass(First_class, Second_class))
# print(issubclass(Second_class, First_class))

# print(isinstance(obj_from_class_2, Second_class))
# print(isinstance(obj_from_class_2, First_class))
#
# print(inspect.ismodule(data))
# print(inspect.isclass(First_class))
# print(inspect.isfunction(Function))
# print(inspect.getmodule(data))


# import sys
#
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.argv)

