import sys


class A:pass

try:
    raise 1

except Exception as e:
    print(e)
    print(sys.exc_info())