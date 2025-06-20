
import os

com_list = []
with os.popen(r'com_pod.bat',"r") as completelist:
    comlist = completelist.readlines()

for i in comlist:
    i2 = i.strip("\n")
    com_list.append(i2)

com_order = []
for j in range(len(com_list)):
    com_order.append(j)

# combine list and order into a dict
com_dict = dict(zip(com_list,com_order))

proxy_list = []
with os.popen(r'proxy_pod.bat',"r") as shinyproxylist:
    proxylist = shinyproxylist.readlines()

for i in proxylist:
    i2 = i.strip("\n")
    proxy_list.append(i2)


sp_list = []
with os.popen(r'shiny_pod.bat',"r") as shinypodlist:
    splist = shinypodlist.readlines()

for i in splist:
    i2 = i.strip("\n")
    sp_list.append(i2)

shiny_order_value = 1

for p in sp_list:
    if com_dict['p'] < shiny_order_value:
        print('ok')
        