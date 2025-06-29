import time
from logging import exception

try:
    f = open('test.i')
    print('~~~~~')
    with f:
        raise exception('1111')
except: # 捕获异常
    print(exception)

# 错误不能被捕获
# 尽可能的捕获和处理各种异常

# try:
#     待捕获异常的代码块
# except[异常类型]:
#     异常的处理代码块

try:
    print('_______________')
    1/0
    print('===============')
#except ZeroDivisionError:
except ArithmeticError:
    print('catch','ZeroDivisionError')
print('outer')

print('----------')