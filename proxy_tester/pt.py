# -*- coding: utf-8 -*-
import requests
from threading import Thread
import re
from bs4 import BeautifulSoup
import time


proxies_ = []


def test(i):
    try:
        proxy = {'https':i}
        get_req1 = str(requests.get('https://passport.yandex.ru/registration/mail?from=mail&origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F', proxies=proxy, timeout=1))
        get_req2 = str(requests.get('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', proxies=proxy, timeout=1))
        get_req3 = str(requests.get('https://www.instagram.com/?hl=rue', proxies=proxy, timeout=1))
        get_req4 = str(requests.get('https://auth.auto.ru/login/?r=https%3A%2F%2Fauto.ru%2F', proxies=proxy, timeout=1))
        if get_req1 == '<Response [200]>' and get_req2 == '<Response [200]>' and get_req3 == '<Response [200]>' and get_req4 == '<Response [200]>':
            print("'%s'," % i)
    except:
        pass

def tester():
    for i in proxies_:
        thr = Thread(target=test, args=(i,))
        thr.start()

def parser():
    page = requests.get('https://www.freeproxy-list.ru/')
    if page.status_code != 200:
        print('Parsing site error')
    else:
        page = page.text
        select_parser = BeautifulSoup(page, 'html.parser')
        find_all_div = str(select_parser.find_all('div', class_='row tr hover'))
        find_all_ip = re.findall(r'\d+[.]\d+[.]\d+[.]\d', find_all_div)
        if len(find_all_ip) != 0:
            for i in find_all_ip:
                proxies_.append('%s:8080' % i)
                tester()
        else:
            print("Proxies haven't found")

        print('\n Press ctrl+c to exit: ')
        while 1:
            tmp = int(input())
            if tmp == 0:
                break


ans = raw_input('Do you wanna check your own proxies?(Y/n): ')
if ans.lower() == 'n':
    print('Sure, trying to find proxies for you...')
    time.sleep(3)
    parser()
elif ans.lower() == 'y':
    print('Enter ip with port 8080 (only ip) | (enter 1 to continue):')
    while 1:
        t = raw_input()
        if t.lower() == '1':
            tester()
        proxies_.append("%s:8080" % t)
else:
    print('Input error')
