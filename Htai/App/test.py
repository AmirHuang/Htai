# _*_ coding: utf-8 _*_
# @time     : 2019/04/12
# @Author   : Amir
# @Site     : 
# @File     : test.py
# @Software : PyCharm


# def f():
#     """
#     这是一个用来测试装饰器修复技术的函数
#     """
#     print("哈哈哈")
#
#
# if __name__ == '__main__':
#     print("执行的函数名:", f.__name__)
#     print("函数的注释:", f.__doc__)

# def wrapper(func):
#     def inner(*args, **kwargs):
#         print("在前面执行的代码。。。。")
#         func()
#         print("在后面执行的代码...")
#     return inner
#
# @wrapper
# def f():
#     """
#         这是一个用来测试装饰器修复技术的函数
#         """
#     print('hhhh')
#
# f()
# print("执行的函数名:", f.__name__)
# print("函数的注释:", f.__doc__)

# from functools import wraps
#
#
# def wrapper(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print("在前面执行的代码。。。。")
#         func()
#         print("在后面执行的代码...")
#
#     return inner
#
#
# @wrapper
# def f():
#     """
#     这是一个用来测试装饰器修复技术的函数
#     """
#     print("哈哈哈")
#
#
# if __name__ == '__main__':
#     print("执行的函数名:", f.__name__)
#     print("函数的注释:", f.__doc__)
#     f()
# username = 1
# password = None
#
# if not all([username, password]):
#     print('sdfsd')
# else:
#     print(315)
# a = 1
# if a in range(2, 10):
#     print('asda')
# else:print(5545)