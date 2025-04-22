# class Calculator:
#     @staticmethod
#     def add(*args):
#         return sum(args)
#
#     @staticmethod
#     def multiply(*args):
#         result = 1
#         for value in args:
#             result *= value
#         return result
#
#     @staticmethod
#     def divide(*args):
#         result = args[0]
#         for value in range(1,len(args)):
#             result /= args[value]
#         return result
#
#     @staticmethod
#     def subtract(*args):
#         result = args[0]
#         for value in range(1, len(args)):
#             result -= args[value]
#         return result
#

from functools import reduce

class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x,y:x+y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)