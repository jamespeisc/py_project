import argparse
from pathlib import Path
import datetime

parser = argparse.ArgumentParser()  # 默认是.py本身
parser = argparse.ArgumentParser(prog='ls', description='ls ', add_help=True)  # 自己添加，就是添加的
# print(parser.prog)
parser.add_argument('path', nargs='?', default='.', help='help path argu')  # 传参
parser.add_argument('-l', action='store_true')
parser.add_argument('-a', '--all', action='store_true')
parser.print_help()

print('~~~~~~~~~~~~~~~~')

args = parser.parse_args('-l  -a '.split())
# print(1, args, type(args))

p = Path(args.path)


def listdir(p: Path, all=False):
    for f in p.iterdir():
        if not all and p.name.startswith('.'):
            continue
        yield f.name


def _getfiletype(p: Path):
    if p.is_dir():
        return 'd'
    elif p.is_symlink():
        return 'l'
    elif p.is_block_device():
        return 'b'
    elif p.is_char_device():
        return 'c'
    elif p.is_socket():
        return 's'
    elif p.is_file():
        return '-'
    else:
        return '-'

modes = 'rwxrwxrwx'

def _getmode(m:int):
    mode=oct(m)[-3:]
    print(mode)
    for c in mode:
        for t in bin(int(c))[-3:]:


def listdirdetail(p:Path, all=False):
    for f in p.iterdir():
        if not all and p.name.startswith('.'):
            continue
        st = f.stat()
        print(st)
        t = _getfiletype(f)
        mode = _getmode(st.st_mode) #
        atime=datetime.datetime.fromtimestamp(st.st_atime).strftime("%Y-%m-%d" %H:%M:%S")
        print(atime)


listdirdetail(p)
