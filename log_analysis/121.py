import configparser
import json

src = 'file/test.ini'
dst = 'file/test.json'
cfg = configparser.ConfigParser()
cfg.read(src)

d = {} #嵌套结构，来自cfg内部的字典

for k, v in cfg.items():
    print(k)
    print(cfg.items(k))
    d[k]=dict(cfg.items(k))
# print(d)

with open(dst, 'w') as f:
    json.dump(d,f)