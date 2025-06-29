import argparse
parser = argparse.ArgumentParser() #默认是.py本身
parser = argparse.ArgumentParser(prog='ls',description='ls ',add_help=True) #自己添加，就是添加的
# print(parser.prog)
parser.add_argument('path',nargs='?',default='.',help='help path argu') #传参
parser.add_argument('-l',action='store_true')
parser.add_argument('-a','--all',action='store_true')
parser.print_help()

print('~~~~~~~~~~~~~~~~')

args = parser.parse_args('/etc -l  -a '.split())
print(1, args, type(args))
# print(args.path, args.path1)
#help 表示文档中这个参数的描述
#nargs 表示这个参数接收结果参数，？表示可有可无，+表示至少一个，*可以任意个，数字表示必须是指定数目个