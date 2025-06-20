
line = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" 
"Mozilla/5.0 (compatible; EasouSpider; +https://www.easou.com/search/spider.html)"'''


def _makekey2(key: str, chars=None):
    if chars is None:
        chars = set(""" \r\n\t""")
    start = 0
    for i, c in enumerate(key):
        if c in chars:
            if start == i:
                start += 1
                continue
            yield key[start:i]
            start = i + 1

    else:
        if start < len(key):
            yield key[start:]


for x in _makekey2(line):
    print(x)
