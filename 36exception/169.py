# BaseException
#     +--SystemExit
#     +--KeyboardInterrupt
#     +--GeneratorExit
#     +--Exception
#         +--RuntimeError
#             +--RecursionError

# 自定义异常

class MyExceptionError(Exception):pass
    # def __init__(self,code,message):
    #     self.code = code
    #     self.message = message

try:
    if 2 == 2:
        raise MyExceptionError(404,'error')
    print('-----')
except MyExceptionError as e:
# except LookupError as e:  # 未捕获的化，用exc捕获
    try:
        print('catch','MyExceptionError',e,e.args)
    except Exception as ee:
        print(ee)
except Exception as e:
    print('catch',e)
finally: # 最终一定要执行
    print('fin')


f = None

try:
    f = open('text1.txt')
except FileNotFoundError as e:
    print(2, e)
finally:
    print('--------------')
    if f:
        f.close()

def foo():
    try:
        print('___________')
        return 100
    except FileNotFoundError as e:
        print(e)
    finally:
        print('fin')
        return 200  #打印 fin 200 ,先打印finally 再return
print(foo())