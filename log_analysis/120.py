d = {}
with open('sample',encoding='utf8') as f:
    for line in f:
        for word in map(makekey1,line):
            d[word] = d.get(word,0) +1