# Lesson 7 about Iters

# my_list = [1, 2, 3]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

#
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
# Count = Counter(5)
#
# for elem in Count:
#     print(elem)
#
# print(Count.__next__())
# print(Count.__iter__())
#
# print(next(Count))
# print(iter(Count))
# print(next(Count))

# def raise_to(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
#
#
# res = raise_to(123456, 10)
# print(res)
# for _ in res:
#     print(_)

#
# class helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"1 - {self.work}, 2 - {work}"
#
# helper_call = helper("Homework")
#
# print(helper_call("cleaning"))

# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"1 - {work}, 2 - {work_in_memory}"
#     return helper
# helper = helper("Homework")
#
# print(helper("cleaning"))


# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(exc)
#         else:
#             print(f"No problem - {result}")
#     return checker

# def calculate(expression):
#     return eval(expression)
# @checker
# def calculate(expression):
#     return eval(expression)
# calculate = checker(calculate)
# calculate("2 + 5")

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    def __next__(self):
        while self.current < self.limit:
            if self.current %2 == 0:
                even_number = self.current

                self.current += 1
                return even_number
        raise StopIteration

iteration = Calculator(10)

for num in iteration:
    print(num)
