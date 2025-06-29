import logging

FORMAT = '%(asctime)s\t [%(threadName)s, %(thread)d] %(message)s '
logging.basicConfig(level=logging.INFO, format=FORMAT,datefmt='%Y%m%d|%H%M%S',filename='logtest.txt',filemode='w')
logging.debug('debug')
logging.info('info111', extra={'school':'magedu.com','ip':'1'})
logging.info('{} {}'.format('info','magedu.com'))
#logging.info('%s %s','info','magedu.com')

# 调用logging.basicConfig来调整级别，本质是根logger对象级别

logger1 = logging.getLogger(__name__)
print(logger1.name)
root = logging.Logger.root
print(logger1)
print(root)
logging.info('main info')
logging.debug('main debug')

print(logger1.getEffectiveLevel())
logger1.setLevel(10)
logger1.debug('main debug')

print(logger1, logger1.level,id(logger1.parent),id(root))
print(root,root.level,id(root.parent))

#自己定义的logger 父为 root

log2 = logging.getLogger(__name__ + '.child')
print(id(log2.parent),id(logger1))

#
# Handler 控制日志信息的输出目的地，可以是控制台，文件
# 可以单独设置level 可以单独设置格式 可以设置过滤器
# 一个logger 可以有多个handler
handler = logging.FileHandler('log.log','w')
logger1.addHandler(handler)
logger1.info('log1 hello')
logger1 = logging.getLogger('log1main') # 获得名字

fmt = logging.Formatter('Log1 ~~~~~ %(message)s')
handler.setFormatter(fmt)
# logger实例，如果设置了level，就用它和信息的级别比较，否则，继承最近的祖先的level