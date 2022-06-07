import requests

proxy_list = []

with open('proxy.txt') as f:
    for line in f:
        proxy_list.append(line.strip())

CRED = '\033[91m'
CEND = '\033[0m'

wordking_proxies = []
for i in proxy_list:
    try:
        proxy = {
            'http':'http://' + i, # http://ip:port
            'https':'http://' + i
        }
        r = requests.get('https://example.com', proxies = proxy)
        wordking_proxies.append(i)
        print('\x1b[6;30;42m' + 'SUCCESS!' + '\x1b[0m' + ' : ' + i)
    
    except:
        print(CRED + "NO" + CEND + ' : ' + i)
        pass

print(wordking_proxies)
