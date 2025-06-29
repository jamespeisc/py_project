import configparser
filename = 'mysql.ini'
cfg = configparser.ConfigParser()
cfg.read(filename)
sections = cfg.sections()
print(sections)
print('!!!!!!!!!!!!')
for sect in sections:
    print(sect, type(sect))
    options = cfg.options(sect)
    print(options, type(options))
    for option in options:
        val = cfg.get(sect,option)
        print(sect,'/', option,'=',val,type(val))
port = cfg.getint('cmdb-database','port')
print(type(cfg.getint('cmdb-database','port')))
print('###################################')
for item in cfg.items():   #cfg.items, kv对
    print(item, cfg.items(item[0]))
print('###################################')
for k,_ in cfg.items():
    print(k, cfg.items(k))

print('###################################')
print(cfg._sections)
print(cfg.sections()) #把keys 转化成list，内部是字典,所以可索引，把自己写的类，作为列表或字典一样访问，称为容器化
print(cfg['cmdb-database']['a'])
print('以上为读')

cfg['cmdb-database']['a'] = '2000'  #ini 内容为字符串

print(cfg['cmdb-database']['a'])
# cfg.add_section('mytest')
cfg['mytest']['a'] = '1000'
with open('mysql.ini','w') as f:
    cfg.write(f)

cfg['test2'] = {'test2': '1000'} #设置内容

print('x' in cfg['test'])
print('x' in cfg['test2'])



