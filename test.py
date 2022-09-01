import os
import random
from httpcore import SyncHTTPProxy

proxy_list=[]
proxy_dir={}

with open('E:\h4cksldkflsldlf\Proxy\workproxy.txt', 'r', encoding='utf-8') as p:
    for proxy in p:
        # IP, port = proxy.strip().split(':')
        # proxy_list.append([IP, port])
        # proxy_dir[IP]=port
        proxy_list.append('http://'+proxy.strip())

    print(proxy_list)
    print(len(proxy_list))
    print(proxy_list[0])

# print(proxy_list[0][0])
# for i in range(10):
#     print(proxy_list[random.randint(0,len(proxy_list))])

# print(proxy_dir)